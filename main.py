#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils  import console, IO, datetimes
from my_word_counter.count import count
from ocurrence import Ocurrence

import time
import json
import argparse
from tinydb import TinyDB, Query

# https://softwareengineering.stackexchange.com/questions/235175/are-closures-considered-impure-functional-style
db = TinyDB('./db.json', sort_keys=True, indent=4)
query = Query()
currentDate = time.time()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Given a json read files and words to be found inside of them.')

    parser.add_argument('json',
                        help="""{

                            "filenames":["theTargeFile1","targetfile2"],
                            "words":[
                                "escribir","todas","las palabras a buscar"
                            ]
                        }"""
                        )


    # argument parsing
    args = parser.parse_args()
    parsed_args =  json.loads(args.json)

    filenames = parsed_args["filenames"]
    words = parsed_args["words"]

    # data retrieving
    files_contents = [(IO.read_function(filename),filename) for filename in filenames]

    def show(result):
        console.message(result, console.bold)
    def persist(filename, word, ocurrences):
        db.upsert({

        'date': currentDate,
        'ocurrence': {
            'filename': filename,
            'ocurrences': ocurrences,
            'word': word
            }
        },
        (query.filename == filename) & (query.word == word))
        #db.insert({'filename': filename, 'data': {'ocurrences': ocurrences, 'word': word}})

    console.paragraph("now:", console.header)
    for (content, filename) in files_contents:
        for word in words:
            ocurrences = count(content, word)
            result = Ocurrence(filename, word, ocurrences)
            show(str(result))
            persist(filename, word, ocurrences)


    console.top("past 10 results for the following files:", console.header)
    for filename in filenames:
        console.message("\t" + filename, console.warning)

    from itertools import groupby
    def showLastNSearchesResults(N):
        for filename_index, filename in enumerate(filenames):
            query_result = db.search(query.ocurrence.filename == filename)
            print


            # for example if you need to get data grouped by each third element you can use the following code
            searches = [list(v) for l,v in groupby(query_result, lambda result: result["date"])]# use date for grouping
            for search_index, search in enumerate(reversed(searches[0:N])):
                search_title = str(search_index + 1) + " " +  datetimes.toHuman(search[0]["date"])
                console.message(search_title, console.bold)
                for result_index, search_result in enumerate(search):
                    filename = search_result['ocurrence']["filename"]
                    word = search_result['ocurrence']["word"]
                    ocurrences = search_result['ocurrence']["ocurrences"]
                    ocurrence = Ocurrence(filename, word, ocurrences)
                    print "\t" + str(ocurrence)
                    #console.message(filename, console.warning)
                    #console.message(query_result, console.identity)

    showLastNSearchesResults(10)
