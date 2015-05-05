import re, sys

def main():
	description_pattern = re.compile("<description>(.*)</description>", re.DOTALL | re.IGNORECASE)

	filename = "./templates/F1_INVITE_call_est.txt"
	with open(filename) as fname:
		fname_content = fname.read()
	description = description_pattern.search(fname_content)
	if not description:
		raise Exception, "Cannot find description, check if it's properly formated: \"<description>Here should be a description</description>\""
	description = description.group(1).strip()
	description = re.sub('\s+', ' ', description)
	template_content = re.sub(description_pattern, '', fname_content).strip()

	print "template is: \n", template_content
	print "Description is:\n", description

if __name__ == "__main__":
	main()

