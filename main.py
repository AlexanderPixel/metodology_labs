from sys import argv
import interactive_mode
import file_mode

if len(argv) < 2:
    interactive_mode.main()
elif len(argv) == 2:
    file_mode.main(argv[1])
else: 
    print('You can pass only 0 or 1 paths of files')