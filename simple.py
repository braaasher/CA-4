# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

data = [line.strip() for line in open(changes_file, 'r')]

sep = 72*'-'

# create the commit class to hold each of the elements - there should be 422
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

#print(len(commits))


#commits.reverse()

#for index, commit in enumerate(commits):
 #   print(commit.get_commit_comment()


def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parsing each of the commits and putting them into a list of commits
            details = data[index + 1].split('|')
            # with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
	
def get_authors(data):
    sep = 72*'-'
    authors = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a list of authors
            author = data[index + 1].split('|')[1].strip()
            if author in authors:
                authors[author] = authors[author] + 1
            else: 
                authors[author] = 1
                index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
	
def get_date(data):
    sep = 72*'-'
    dates = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a list of authors
            date = data[index + 1].split('|')[2].strip()
            dates.append(date)
            index = data.index(sep, index + 1)     
        except IndexError:
            break
    return dates   

    
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    #print(len(data))
    #print(commits)
    #print(commits[0])
    print(commits[1]['author'])
    print(commits[2]['author'])
    print(commits[3]['author'])
    print(len(commits[0]['author']))
    

    
    #print(len(commits))
    #print(len(commits[0]['author']))
    #print(len(commits[0]['date']))
   # print get_date(data)
    #print len(get_date(data))
