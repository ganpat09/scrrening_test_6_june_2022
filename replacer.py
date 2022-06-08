import logging
import re
from fileinput import FileInput
import sys

formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                              '%m-%d %H:%M:%S')

logging.basicConfig(filename='screening.log', encoding='utf-8', level=logging.DEBUG, filemode="a+")


class Replacer:
    """Replacer is use for replace the content from text file"""

    def __init__(self, file_name, replace_content_or_regex, replaced_into):
        """ File name: example.txt
            Origin file content:

            This is a placement assignment

            Replace string Placement should be replaced by screening.
            Replaced file content:

            This is a screening assignment

            @replace_content support regex also

            """

        self.file_name = file_name
        self.replace_content = replace_content_or_regex
        self.replaced_into = replaced_into

    def do_replacement(self):
        """start replacement"""

        try:
            with FileInput(self.file_name, inplace=True) as f:

                for line in f:
                    sys.stdout.write(line.replace(line, re.sub(self.replace_content, self.replaced_into, line, flags=re.IGNORECASE)))
                    logging.info("Successfully replaced")



        except Exception as e:
            print(e)
            logging.error(e)


if __name__ == "__main__":
    # dummy purpose add file in starting
    with(open("example.txt", "w+")) as f:
        f.write("This is a placement assignment  ")

    replacer = Replacer("example.txt", "Placement", "screening")
    replacer.do_replacement()


