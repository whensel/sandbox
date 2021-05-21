key = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

def arabicToRoman(number: int) -> str:

    #simple catch all
    if locate_in_key(number) != None:
        return locate_in_key(number)

    response = subtraction_process(number)


    return response

#finds the number in the key if possible
def locate_in_key(number: int) -> str:
    for roman_numeral in key:
        if key[roman_numeral] == number:
            return str(roman_numeral)

# subtracts key numbers from main number until result is converted fully
def subtraction_process(number: int) -> str:
    response = ''
    
    while number >= 0:
        for numbers in key:
            if number - key[numbers] >= 0:
                number = number - key[numbers]
                key_reference = key[numbers]
                response = response + locate_in_key(key_reference)
                
                break
        if number == 0:
            return response
        else:
            pass






### my previous attempts ###
# converted = number_breakdown(number)
# print(converted)
#
# for items in converted:
#     for roman_numeral in key:
#         if key[roman_numeral] == items:
#             response = response + str(roman_numeral)
#         else:
#             while items != 0:
#                 for roman_numeral in key:
#                     if items - key[roman_numeral] > 0:
#                         response = response + locate_in_key(items)
#                         items = items - key[roman_numeral]


# while x >= 0:
# for numbers in key:
#     if x - key[numbers] >= 0:
#         sub_result = x - key[numbers]
#         roman_numeral = locate_in_key(key[numbers])
#         x = x - sub_result
#         response = response + roman_numeral
#     else:
#         pass


# def number_breakdown(number: int) -> [int]:
#     num_list = list(map(int, str(number)))
#     num_list_expanded = convertToTensPlaces(num_list)
#
#     return num_list_expanded
#
#
# def convertToTensPlaces(num_list: [int]) -> [int]:
#     num_length = len(num_list)
#     zeros_list = add_zeros(num_length)
#
#     for x in range(num_length):
#         num_list[x] = num_list[x] * zeros_list[x]
#
#     return num_list
#
#
# def add_zeros(num_length: int) -> [int]:
#     zeros_list = []
#
#     while num_length > 0:
#         total_zeros = ''
#         for i in range(num_length-1):
#             total_zeros = total_zeros + "0"
#         zeros_list.append(int("1" + total_zeros))
#
#         num_length = num_length - 1
#
#     return zeros_list
