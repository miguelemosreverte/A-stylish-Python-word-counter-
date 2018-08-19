pip install -r requirements.txt
echo "Merged install.sh and run.sh for your confort, it's not routine."
clear; echo "...aaand clear!"

python main.py '{

              "filenames":["examples/corpus.md", "examples/enoughApples.md"],
              "words":[
                   "banana", "apple", "zebra"
              ]
          }'
