__author__ = "marc"

from textrazor import TextRazor
from Analyzers import HyperLink, DbpediaLink


def process_textrazor_api(text):
    client = TextRazor(
        api_key='67ef1ca06614f7d202b23f1444bd7ee1ea2f916b3ecf488f8d39f800',
        extractors=[
            "entities",
            "topics",
            "words",
            "phrases",
            "dependency-trees",
            "senses"
        ]
    )

    try:
        response = client.analyze(text)
    except:
        return []

    link_matches = HyperLink.extract_all_url(text)

    initial_entities = []
    for entity in response.entities():
        possible_link = False
        for link_match in link_matches:
            if link_match["start"] <= entity.starting_position and link_match["end"] >= entity.ending_position:
                possible_link = True

        if not possible_link:
            e = {
                "label": entity.matched_text,
                "startOffset": entity.starting_position,
                "endOffset": entity.ending_position,
                "confidence": entity.confidence_score,
                "relevance": entity.relevance_score,
                "provenance": "textrazor",
                "wikipediaLink": entity.wikipedia_link,
                "types": []
            }

            for dbpedia_type in entity.dbpedia_types:
                wiki_link = "http://en.wikipedia.org/wiki/" + dbpedia_type

                dbpedia_type_list = {
                    "typeURI": None,
                    "typeLabel": dbpedia_type,
                    "wikiURI": wiki_link,
                    "entityURI": DbpediaLink.get_english_resource_from_english_wikipedia_link(wiki_link),
                    "confidence": entity.confidence_score
                }

                e["types"].append(dbpedia_type_list)

            for freebase_type in entity.freebase_types:
                freebase_link = "http://www.freebase.com" + freebase_type

                freebase_type_list = {
                    "typeURI": None,
                    "typeLabel": "Freebase:" + freebase_type.replace(" ", ""),
                    "wikiURI": None,
                    "entityURI": freebase_link,
                    "confidence": entity.confidence_score
                }

                e["types"].append(freebase_type_list)

            wiki_type_list = {
                "typeURI": None,
                "typeLabel": [],
                "wikiURI": entity.wikipedia_link,
                "entityURI": DbpediaLink.get_english_resource_from_english_wikipedia_link(entity.wikipedia_link),
                "confidence": entity.confidence_score
            }

            e["types"].append(wiki_type_list)

            initial_entities.append(e)

    return initial_entities


def read_api_key():
    try:
        lines = [line.strip() for line in open('Config/textrazor.cfg')]
        return lines[0]
    except:
        print "No textrazor.cfg file found in /Config or no api key on the first line of the file."
        exit()