PLACEHOLDER='[name]'


with open(r"mail_merge\datas\names.txt") as names_file:
    names=names_file.readlines()
    
with open(r"mail_merge\datas\mail_template.txt") as template:
    template_content=template.read()
    for name in names:
        stripped_name=name.strip("\n")
        new_name_letter=template_content.replace(PLACEHOLDER,stripped_name)
        with open (f"mail_merge\\ready_to_send\\letter_for_{stripped_name}.txt",mode="w") as revised_letter:
            revised_letter.write(new_name_letter)