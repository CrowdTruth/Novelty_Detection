__author__ = "marc"

import spotlight
from Analyzers import HyperLink, DbpediaLink


def process_spotlight_api(text):
    try:
        entities = spotlight.annotate(
            "http://spotlight.dbpedia.org/rest/annotate",
            text,
            confidence=0.1,
            support=0
        )
    except:
        return []

    link_matches = HyperLink.extract_all_url(text)

    initial_entities = []
    for entity in entities:
        occ = 0
        if occ is not 0:
            occ = text.count('"', 0, entity["offset"] + len(entity["serviceForm"]) - 1)
        start = entity["offset"] + occ
        end = entity["offset"] + len(entity["surfaceForm"]) + occ

        possible_link = False
        for link_match in link_matches:
            if link_match["start"] <= start and link_match["end"] >= end:
                possible_link = True

        if not possible_link:
            e = {
                "label": entity["surfaceForm"],
                "startOffset": start,
                "endOffset": end,
                "confidence": entity["similarityScore"],
                "provenance": "dbpediaspotlight",
                "types": []
            }

            types = []
            for data_type in entity["types"].split(","):
                link = data_type
                if "DBpedia:" in data_type:
                    link = "http://en.dbpedia.org/resource/" + data_type.split(":")[1]
                if "Freebase:" in data_type:
                    link = "http://www.freebase.com" + data_type.split(":")[1]

                dbpedia_type = {
                    "typeURI": None,
                    "typeLabel": data_type,
                    "entityURI": link,
                    "confidence": entity["similarityScore"],
                    "wikiURI": DbpediaLink.get_english_wikipedia_link_from_english_resource(link)
                }
                types.append(dbpedia_type)

            e["types"].append(types)
            initial_entities.append(e)

    return initial_entities
