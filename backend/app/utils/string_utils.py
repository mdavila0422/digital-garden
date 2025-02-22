import re
from functools import reduce  
    
def string_truncator(string: str, max_length: int, word_boundary: bool = False) -> str:
    # Check if truncation is needed at all
    """
    Truncates a string for error message display.
    
    Pre-processing (always applied):
    1. Strip leading/trailing whitespace
    2. Normalize internal whitespace (newlines/tabs to single spaces)
    
    Then either:
    A. If word_boundary=False:
       - Truncate at exactly max_length
       - Add ellipsis if truncated
       
    B. If word_boundary=True:
       - Find the last complete word that fits
       - Add ellipsis if truncated
       
    Always adds ellipsis when content is truncated to indicate more content exists.
        
    2. Supports:
        - Unicode characters (international text)
        - Special characters (@#$% etc)
        - Common punctuation
        
    3. Word boundary mode only splits on:
        - Spaces (including multiple spaces)
        - Common sentence punctuation (., !, ?, ,)
        - Line breaks
        
    All other characters are preserved as-is.
    
    :param string: The string to be truncated
    :param max_length: The maximum length of the string
    :param word_boundary: If True, the string is truncated at the last word boundary preceding max_length. If False, the string is simply truncated at max_length.
    
    :return: The truncated string
    """
    #Pre-processing (always applied):
    string = re.sub("\s+", " ", string).strip()
    # Early return check:
    if len(string) <= max_length:
        return string
    # For non-word boundary truncation, simply truncate at max_length
    elif not word_boundary:
        return string[:max_length].strip() + "..."
    # For word boundary truncation, find the last complete word that fits
    else:
        # clean the string and split into words
        word_list = re.sub("[.,;!?]", " ", string).strip().split()
        # Check if the first word is longer than max_length
        if len(word_list[0]) > max_length:
            return string[:max_length].strip() + '...'
        else:
            # Build truncated string:
            running_length = 0
            final_string = ""
            index = 0
            while index < len(word_list) and running_length <= max_length:
                if running_length + len(word_list[index]) > max_length:
                    final_string = final_string.strip() + '...'
                    break
                else:
                    running_length += len(word_list[index]) + 1
                    final_string += word_list[index] + ' '
                    index += 1
            return final_string.strip()
        
        
