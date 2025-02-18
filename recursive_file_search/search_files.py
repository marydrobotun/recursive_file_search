from recursive_file_search.sources.main import walk
from recursive_file_search.sources.helper_functions import has_even_bytesize

print(walk('.', has_even_bytesize))
