def calculate_area_square(length: int | float) -> float:
    """正の数の辺長から正方形の面積を計算"""
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length
