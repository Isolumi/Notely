from typing import List


def split_text(text: str, max_len: int, min_len: int) -> List[str]:
    words = text.split()
    chunks = []
    current_chunk = []
    
    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_len and len(' '.join(current_chunk)) > min_len:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            
    if current_chunk:
        chunks.append(' '.join(current_chunk))
        
    return chunks