from typing import TextIO


def replacer(first: str, second: str, fitst_file: TextIO, second_file: TextIO) -> None:
	for first_letter in first:
		for second_letter in second:
			fitst_file.write(first_letter)
			fitst_file.write('\n')
			second_file.write(second_letter)
			second_file.write('\n')


def main() -> None:
	with open('PythonTest.txt', 'r', encoding='utf-8') as file, \
			open('output/English.txt', 'a', encoding='utf-8') as eng_file, \
			open('output/Russian.txt', 'a', encoding='utf-8') as rus_file:
		for row in file:
			eng_letters, rus_letters = row.strip().split('\t')
			eng_letters = eng_letters.split(' ; ')
			rus_letters = rus_letters.split(' ; ')
			if len(eng_letters) >= len(rus_letters):
				replacer(eng_letters, rus_letters, eng_file, rus_file)
			else:
				replacer(rus_letters, eng_letters, rus_file, eng_file)

	print('Done!')


if __name__ == "__main__":
	main()
