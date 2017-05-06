
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

#it's either or here above or below (both do same)

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

class Commit(object):

#creating six columns of data

    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
		
a_commit = Commit('rr1551925', 'Thomas', '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', 1, None, 'Renamed folder to the correct name')

print a_commit.revision
print a_commit.author

commits = []
#we will have list of commits once this has run
current_commit = None
#want to run through entire list(index 0 is beginning)
index = 0

#we want to search for separator and 
#read line for revision, author, date, comment line count
#read file changes
#read comment
#get next commit

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
	#print(details)
		#on next line 0 represents 1st part (or first detail) from above, splitting at |
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
		
		#this is essentially what you want the code to do ->
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))
print commits[0].author
print commits[0].changes
print commits[0].comment

commits.reverse()

#for index, commit in enumerate(commits):
    #print(commit.get_commit_comment())

	
	
