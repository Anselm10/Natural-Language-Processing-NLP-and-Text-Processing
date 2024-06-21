from pypdf import PdfReader 
infoes = ['Book/Brief Answers to the Big Questions.pdf',
		  'Book/Reith Lectures 2016_Part1 - Prof S Hawking - Black Holes, Part 1 [25-01-2016].pdf',
		  'Book/Reith Lectures 2016_Part2 - Prof S Hawking - Black Holes, Part 2 [01-02-2016].pdf',
		  'Book/Stephen Hawking - A Brief History Of Time.pdf']

for i in infoes:
	title = '_'.join(i.split('/')[1].split()[0:3]).replace('-','')+'.txt'
	title = 'Book_'+title
	reader = PdfReader('Data_Book/'+i)
	with open('Data_Book/'+title,'a',encoding="utf-8") as f:
		# getting a specific page from the pdf file
		for i in range(1,len(reader.pages)): 
			page = reader.pages[i] 
			# extracting text from page 
			text = page.extract_text() 
			f.write(text) 
print('Success')


Questions = ['Question Answer/500 Data Science Interview Questions and Answers.pdf','Question Answer/Deep Learning Interviews.pdf','Question Answer/The-Handy-Psychology-Answer-Book-1.pdf']

for i in Questions:
	title = '_'.join(i.split('/')[1].split()[0:3]).replace('-','')+'.txt'
	title = 'Question_Answer'+title
	reader = PdfReader('Data_Book/'+i)
	with open('Data_Book/'+title,'a',encoding="utf-8") as f:
		# getting a specific page from the pdf file
		for i in range(1,len(reader.pages)): 
			page = reader.pages[i] 
			# extracting text from page 
			text = page.extract_text() 
			f.write(text) 
print('Success')