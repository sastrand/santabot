msg_template = '''---
layout: blank
permalink: /santabot/{{santa_lower}}/{{santa_uuid}}
---
```
Dear {{santa}},

Your Secret Santa recipient is {{recipient}}!

A reminder of the guidelines:
* give to a cause/non-profit that you think will resonate with {{recipient}}
* don't give to {{recipient}}'s employer (if {{recipient}} works for a non-profit)
* there is no pressure to disclose how much/what you give

On 12/26 we'll meet up on Zoom and share! 🎅

Much love,  
SantaBot/Sascha
```
'''

class FamilyMember:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.quant_elig_recips = 0
    
    def __str__(self):
        return self.name + " " + self.code + " " + str(self.quant_elig_recips)
    
    def __lt__(self, other):
        return self.quant_elig_recips < other.quant_elig_recips
    
    def set_quant_elig_recips(self, n):
        self.quant_elig_recips = n
        

class Family:
    def __init__(self):
        self.family_members = {}
        self.members_by_quant_recips = []
    
    def set_family_member(self, name, family_code):
        family_member = FamilyMember(name, family_code)
        self.family_members[name] = family_member
        self.members_by_quant_recips.append(family_member)
    
    def set_quant_elig_recipients(self):
        # lol n^2
        for p in self.get_names():
            quant_elig_recips = len([p2 for p2 in self.family_members.keys() if self.is_eligible_recipient(p, p2)])
            self.family_members[p].set_quant_elig_recips(quant_elig_recips)
        self.members_by_quant_recips.sort()
    
    def get_family_member_code(self, name):
        return self.family_members[name].code
    
    def is_eligible_recipient(self, santa, recipient):
        return santa != recipient and self.get_family_member_code(santa) != self.get_family_member_code(recipient)
    
    def print_family(self):
        for k in self.members_by_quant_recips:
            print(k)
    
    def get_names(self):
        return [p.name for p in self.members_by_quant_recips]
        
values = {
  ("Papa", "A"),
  ("Eric", "B"),
  ("Jennie", "B"),
  ("Avery", "B"),
  ("Carsten", "B"),
  ("Drew", "B"),
  ("Jon", "C"),
  ("Beth", "C"),
  ("Elizabeth", "C"),
  ("Sarah", "C"),
  ("Mark", "C"),
  ("Paul", "D"),
  ("Kim", "D"),
  ("Sascha", "D"),
}

fam = Family()
for v in values:
    fam.set_family_member(v[0], v[1])
fam.set_quant_elig_recipients()
fam.print_family()

from random import randrange
import uuid

def get_eligible_recipients(santa, fam, recipients_assigned):
    return [p for p in fam.get_names() if fam.is_eligible_recipient(santa, p) and p not in recipients_assigned]

def get_recipient(santa, fam, recipients_assigned):
    elig_recipients = get_eligible_recipients(santa, fam, recipients_assigned)
    recip = elig_recipients[randrange(0, len(elig_recipients))]
    recipients_assigned.add(recip)
    return recip

recipients_assigned = set()
people = [[p, None, None] for p in fam.get_names()]
for person in people:
    person[1] = get_recipient(person[0], fam, recipients_assigned)
    person[2] = str(uuid.uuid4())


from jinja2 import Template
template = Template(msg_template)
uris = []

for p in people:
    note = template.render(santa=p[0], recipient=p[1], santa_lower=p[0].lower(), santa_uuid=p[2])
    file_name = "secret_santa_2022/" + f"{p[0]}.md"
    with open(file_name, "w") as text_file:
        print(note, file=text_file)
    uris.append(f'https://www.queery.io/santabot/{p[0].lower()}/{p[2]}')

for uri in uris:
    print(uri)
