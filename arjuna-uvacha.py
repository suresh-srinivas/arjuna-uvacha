import re

def get_arjuna_verses_by_chapter_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return get_arjuna_verses_by_chapter(text)

def get_arjuna_verses_by_chapter(text):
    lines = text.split('\n')
    chapter_verse_counts = {}
    arjuna_verses_text = {}
    is_arjuna_speaking = False
    arjuna_verses_numbers = [[] for _ in range(18)]

    for line in lines:
        if re.search(r'\bArjuna\b.*?\bsaid:', line):
            is_arjuna_speaking = True
            current_verse = []
        elif 'said:' in line and not re.search(r'\bArjuna\b.*?\bsaid:', line):
            is_arjuna_speaking = False

        if is_arjuna_speaking:
            current_verse.append(line)
            verse_matches = re.findall(r'\((\d+)\.(\d+)\)', line)
            for chapter, verse in verse_matches:
                chapter = int(chapter)
                chapter_index = chapter - 1
                verse_id = f"{chapter}.{verse}"
                arjuna_verses_numbers[chapter_index].append(verse_id)
                chapter_verse_counts.setdefault(chapter, 0)
                chapter_verse_counts[chapter] += 1
                arjuna_verses_text.setdefault(chapter, []).append(' '.join(current_verse))
                current_verse = []

    total_verses = sum(chapter_verse_counts.values())
# After processing all lines
    print("\nChapter-wise Arjuna's verse numbers:")
    for chapter, verses in enumerate(arjuna_verses_numbers, 1):
        if verses:
            print(f"Chapter {chapter}: {verses}")
    return chapter_verse_counts, arjuna_verses_text, total_verses

def format_verses_text(verses_text):
    formatted_text = ""
    for chapter, verses in verses_text.items():
        formatted_text += f"\nChapter {chapter}:\n" + "\n".join(verses) + "\n"
    return formatted_text


# Usage
file_path = 'bhagavad_gita.txt'
chapter_verse_counts, arjuna_verses_text, total_verses = get_arjuna_verses_by_chapter_from_file(file_path)
formatted_text = format_verses_text(arjuna_verses_text)

print(f"Chapter-wise count: {chapter_verse_counts}")
print(f"Total verses by Arjuna: {total_verses}")
print(formatted_text)


