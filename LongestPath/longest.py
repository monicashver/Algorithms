import fileinput

#def is_this_path_longer(root, depth, new_depth, line):



def main():

	curr_depth = 0
	curr_paths = []
	curr_root = '/'

	for line in fileinput.input():

		#clean up whitespace line and get its depth
		line  = line.strip('\n').split(' ')

		#get current depth of item
		new_depth = len(line)

		#if we into a directory
		if(new_depth > curr_depth):
			#update depth
			curr_depth = new_depth
			#add new items to paths
			curr_paths.append(line[-1])

		#we moved up directory/directories
		elif(new_depth < curr_depth):
			#delete all items that are from the old depth
			del(curr_paths[new_depth - 1 : curr_depth])
			#add the new item we just saw
			curr_paths.append(line[-1])
			#update depth
			curr_depth = new_depth

		#if we are looking at files within the same folder
		elif(new_depth == curr_depth):

			#change the last item of current path
			curr_paths[-1] = line[-1]

		#if we found a picture file, compare current longest path with new one
		if(('.jpeg' in line[-1]) or ('.gif' in line[-1]) or ('.png' in line[-1])):
			#create what would be the path of the picture file
			temp =  '/' + '/'.join(curr_paths)
			#update longest file name if new file path is longer
			if(len(temp) > len(curr_root)):
				curr_root = temp

	print(curr_root)
if __name__ == '__main__':
	main()