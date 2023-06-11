def convert_to_range(value, width=640, range_start=1, range_end=9):
    ratio = (value - 0) / (width - 0)
    converted_value = range_start + (range_end - range_start) * ratio
    return round(converted_value)

# 예시 입력 값
value = 320
converted_value = convert_to_range(value, 640, 1, 20)
print(f"{value}는 비율로 변환하면 {converted_value}입니다.")