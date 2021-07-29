import genanki

my_model = genanki.Model(
    2033507265,  #随机唯一id: import random; print(random.randrange(1 << 30, 1 << 31))
    'Simple Model',
    fields=[
        {
            'name': 'Question'
        },
        {
            'name': 'Answer'
        },
        {
            'name': 'audio'
        },
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}<br>{{audio}}',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])
my_note = genanki.Note(
    model=my_model,
    fields=['Capital of Argentina', 'Buenos Aires', '[sound:0_001.mp3]'])
my_deck = genanki.Deck(2059400110, 'Country Capitals')
my_deck.add_note(my_note)

my_package = genanki.Package(my_deck)
my_package.media_files = ['./data/IELTS/crawler/0/0_001.mp3']

my_package.write_to_file('output.apkg')

print(my_note)
