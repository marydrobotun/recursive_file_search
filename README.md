
# File Filter Utility

This Python script provides a set of utility functions to filter files based on specific criteria, such as file size, filename content, and more. It also includes a recursive directory traversal function to apply these filters across a directory structure.
## Features

-   **Check if a file has an even byte size**: The `has_even_bytesize` function determines whether the size of a file is an even number.
    
-   **Check if a filename contains every vowel**: The `has_every_vowel` function checks if the filename (without extension) contains all vowels (a, e, i, o, u).
    
-   **Check if a file size is greater than a specified minimum size**: The `is_size_more_than` function checks if the file size exceeds a given threshold.
    
-   **Check if a file size is less than a specified maximum size**: The `is_size_less_than` function checks if the file size is below a given threshold.
    
-   **Recursively walk through a directory and filter files**: The `walk` function traverses a directory and collects file paths that satisfy a given filter function. 
> **_NOTE:_** Filter function can be chosen from listed above or you can use your own filter function.
## Functions

### `has_even_bytesize(path: str) -> bool`

-   **Description**: Checks if the file at the given path has an even byte size.
    
-   **Parameters**:
    
    -   `path` (str): The path to the file.
        
-   **Returns**: `True` if the file size is even, `False` otherwise.
    

### `has_every_vowel(path: str) -> bool`

-   **Description**: Checks if the filename (without extension) contains every vowel (a, e, i, o, u).
    
-   **Parameters**:
    
    -   `path` (str): The path to the file.
        
-   **Returns**: `True` if the filename contains all vowels, `False` otherwise.
    

### `is_size_more_than(path: str, minsize: int = 1000) -> bool`

-   **Description**: Checks if the file size is greater than the specified minimum size.
    
-   **Parameters**:
    
    -   `path` (str): The path to the file.
        
    -   `minsize` (int): The minimum size threshold (default is 1000 bytes).
        
-   **Returns**: `True` if the file size is greater than `minsize`, `False` otherwise.
    

### `is_size_less_than(path: str, maxsize: int = 1000) -> bool`

-   **Description**: Checks if the file size is less than the specified maximum size.
    
-   **Parameters**:
    
    -   `path` (str): The path to the file.
        
    -   `maxsize` (int): The maximum size threshold (default is 1000 bytes).
        
-   **Returns**: `True` if the file size is less than `maxsize`, `False` otherwise.
    

### `walk(folder: str, filter_func: Callable[[Any], bool]) -> list[str]`

-   **Description**: Recursively walks through a directory and collects file paths that satisfy a given filter function.
    
-   **Parameters**:
    
    -   `folder` (str): The path to the directory to traverse.
        
    -   `filter_func` (Callable[[Any],bool]): A function that takes a file path and returns a boolean indicating whether  
 the file should be included in the result.
        
-   **Returns**: A list of file paths that satisfy the filter function.
## Usage
For example:
```
import os

from recursive_file_search.sources.main import walk  
from recursive_file_search.sources.helper_functions import has_even_bytesize, is_size_less_than

filtered_files = walk("example_directory", has_even_bytesize)
print("Files with even byte size:", filtered_files)
```

## Requirements

-   Python 3.x
    
-   Standard Python libraries (`os`, `typing`)
    

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE) file for details.
