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

    for line in lines:
        # Check if the line indicates Arjuna starts speaking
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
                chapter_verse_counts.setdefault(chapter, 0)
                chapter_verse_counts[chapter] += 1
                arjuna_verses_text.setdefault(chapter, []).append(' '.join(current_verse))
                current_verse = []

    return chapter_verse_counts, arjuna_verses_text

def test_arjuna_verses():
    text = """
    Sanjaya said: O King, Lord Krishna, as requested by Arjuna, placed the best of all the chariots in the midst of the two armies; (1.24)
    Facing Bheeshma, Drona, and all other Kings; and said to Arjuna: Behold these assembled Kurus! (1.25)
    Arjuna said: How shall I strike Bheeshma and Drona, who are worthy
    of my worship, with arrows in battle, O Krishna? (2.04)
    Arjuna the mighty said: It would be better, indeed, to live on alms in this world than to
    slay these noble gurus, because, by killing them I would enjoy
    wealth and pleasures stained with (theirs) blood. (2.05)
    Arjuna was overcome with great compassion and sorrowfully said:
    Neither do we know which alternative (to beg or to kill) is better
    for us, nor do we know whether we shall conquer them or they will
    conquer us. (2.06)
    Sanjaya said: O King, after speaking like this to Lord Krishna, the
    mighty Arjuna said to Krishna: I shall not fight, and became
    silent. (2.07)
    There Arjuna saw his uncles, grandfathers, teachers, maternal uncles, brothers, sons, grandsons, and comrades. (1.26)
    Seeing fathers-in-law, all those kinsmen, and other dear ones standing in the ranks of the two armies, (1.27)
    """

    verse_count, verses_text = get_arjuna_verses_by_chapter(text)
    print(verse_count)
    for chapter, verses in verses_text.items():
        print(f"Chapter {chapter}:")
        for verse in verses:
            print(verse)

test_arjuna_verses()


