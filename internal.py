#%%
participants = [
"mohadesa-abdullahi",
"denise-argyropoulos",
"amina-bijbulatova",
"dalya-dalfi",
"iman-germekhanova",
"zakiye-hojati",
"marcella-loidl",
"neelam-malik",
"mahsa-mohammadi",
"melina-muratovic",
"zynet-nasser",
"samira-schachabova",
"sara-soukkar",
"aisha-yousaf",
"hala-zarzory",
"dajana-zivanovic"
]
#%%
import os

for participant in participants  :
    path = f"{os.path.join('source/participants', participant)}.md"

    title = participant.replace('-', ' ')
    title = title.title()
    with open(path, 'w') as fh:
        fh.write(f'# {title}')


# %%
