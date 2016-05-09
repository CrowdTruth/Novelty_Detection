__author__ = "marc"

from Libraries import nerd
from Analyzers import HyperLink, DbpediaLink
import urllib


def process_nerd_api(text):
    try:
        timeout = 10
        text = urllib.quote_plus(text)
        n = nerd.NERD("nerd.eurecom.fr", 'akkqfgos0p85mcubcfgp82rn92d23enu')
        entities = n.extract(text, "combined", timeout)
    except:
        return []

    link_matches = HyperLink.extract_all_url(text)

    initial_entities = []
    for entity in entities:
        possible_link = False
        for link_match in link_matches:
            if link_match["start"] <= entity["startChar"] and link_match["end"] >= entity["endChar"]:
                possible_link = True

        if not possible_link:
            e = {
                "label": entity["label"],
                "startOffset": entity["startChar"],
                "endOffset": entity["endChar"],
                "confidence": entity["confidence"],
                "provenance": "nerd-" + entity["extractor"],
                "types": []
            }

            if entity["extractorType"]:
                all_types = entity["extractorType"].split(",")

                for extracted_type in all_types:

                    if "dbpedia" in extracted_type:
                        type_data = {
                            "typeURI": extracted_type,
                            "typeLabel": None,
                            "wikiURI": DbpediaLink.get_english_resource_from_english_wikipedia_link(entity["uri"]),
                            "entityURI": entity["uri"],
                            "confidence": entity["confidence"]
                        }
                    else:
                        type_data = {
                            "typeURI": None,
                            "typeLabel": extracted_type,
                            "wikiURI": DbpediaLink.get_english_resource_from_english_wikipedia_link(entity["uri"]),
                            "entityURI": entity["uri"],
                            "confidence": entity["confidence"]
                        }

                    e["types"].append(type_data)

                if entity["nerdType"]:
                    nerd_type_data = {
                        "typeURI": entity["nerdType"],
                        "typeLabel": entity["nerdType"].split("#")[1],
                        "wikiURI": DbpediaLink.get_english_resource_from_english_wikipedia_link(entity["uri"]),
                        "entityURI": entity["uri"],
                        "confidence": entity["confidence"]
                    }

                    e["types"].append(nerd_type_data)

            initial_entities.append(e)

    return initial_entities


def read_api_key():
    try:
        lines = [line.strip() for line in open('Config/nerd.cfg')]
        return lines[0]
    except:
        print "No nerd.cfg file found in /Config or no api key on the first line of the file."
        exit()