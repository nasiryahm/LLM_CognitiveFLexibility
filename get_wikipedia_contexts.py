import wikipedia
import csv
import context_creator


wikipedia.set_lang("en")

num_articles = 100  # Set to 100 for full run

with open("contexts.csv", "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(num_articles):
        try:
            random_title = wikipedia.random(1)
            page = wikipedia.page(random_title)
            summary = page.summary.replace("\n", " ").strip()
            title = page.title.replace(" ", "_")
            if summary:  # Only add if there's content
                writer.writerow([title, "clean", summary])
                ms = context_creator.meaningful_shuffle(summary)
                writer.writerow([title, "meaningful_shuffle", ms])
                ws = context_creator.word_shuffle(summary)
                writer.writerow([title, "word_shuffle", ws])
                cs = context_creator.character_shuffle(summary)
                writer.writerow([title, "char_shuffle", cs])
                print(f"Added article {i+1}: {title}")
            else:
                print(f"Skipped article {i+1}: no summary")
        except Exception as e:
            print(f"Error on article {i+1}: {e}")

print(f"Finished adding {num_articles} articles.")
