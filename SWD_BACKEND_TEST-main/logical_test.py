
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def convert_num_to_thai_text() :
    i_num = int(input('Enter your number : '))
    v_conv_text = ['','สิบ','ร้อย','พัน','หมื่น','แสน','ล้าน']
    v_thai_num_list = ['ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']

    v_list_num = [int(x) for x in str(i_num)]
    v_thai_name = ''
    if i_num >= 0 and i_num < 10000000 :
        if len(v_list_num) == 1 :
            print('Convert number to thai text : '+ str(v_thai_num_list[v_list_num[0]]))
        else:
            for i in range(0,len(v_list_num)):

                if  v_list_num[i] == 0 :
                    pass
                elif len(v_list_num)-i-1 == 0 and v_list_num[i] == 1 :
                    v_thai_name = v_thai_name +'เอ็ด'
                elif len(v_list_num)-i-1 == 1 :
                    if v_list_num[i] == 1 :
                        v_thai_name = v_thai_name  + str(v_conv_text[len(v_list_num)-i-1]) 
                    elif v_list_num[i] == 2:
                        v_thai_name = v_thai_name +'ยี่' + str(v_conv_text[len(v_list_num)-i-1])
                    else : 
                        v_thai_name = v_thai_name + str(v_thai_num_list[v_list_num[i]]) + str(v_conv_text[len(v_list_num)-i-1])
                else : 
                    v_thai_name = v_thai_name + str(v_thai_num_list[v_list_num[i]]) + str(v_conv_text[len(v_list_num)-i-1])

        print('Convert number to thai text : ' + v_thai_name)
    else :
        print('The number is not in range 0-9999999 can not convert to thai text ')

#     if __name__ == '__main__':
#         convert_num_to_thai_text()



# i_num = int(input('Enter your number : '))
# v_conv_text = ['','สิบ','ร้อย','พัน','หมื่น','แสน','ล้าน']
# v_thai_num_list = ['ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']

# v_list_num = [int(x) for x in str(i_num)]
# v_thai_name = ''

# if i_num >= 0 and i_num < 10000000 :
#     if len(v_list_num) == 1 :
#         v_thai_name= str(v_thai_num_list[v_list_num[0]])
#     else:
#         for i in range(0,len(v_list_num)):
        

#             if  v_list_num[i] == 0 :
#                 pass
#             elif len(v_list_num)-i-1 == 0 and v_list_num[i] == 1 :
#                 v_thai_name = v_thai_name +'เอ็ด'
#             elif len(v_list_num)-i-1 == 1 :
#                 if v_list_num[i] == 1 :
#                     v_thai_name = v_thai_name  + str(v_conv_text[len(v_list_num)-i-1]) 
#                 elif v_list_num[i] == 2:
#                     v_thai_name = v_thai_name +'ยี่' + str(v_conv_text[len(v_list_num)-i-1])
#                 else : 
#                     v_thai_name = v_thai_name + str(v_thai_num_list[v_list_num[i]]) + str(v_conv_text[len(v_list_num)-i-1])
#             else : 
#                 v_thai_name = v_thai_name + str(v_thai_num_list[v_list_num[i]]) + str(v_conv_text[len(v_list_num)-i-1])

#     print('Convert number to thai text : ' + v_thai_name)
# else :
#     print('The number is not in range 0-9999999 can not convert to thai text ')