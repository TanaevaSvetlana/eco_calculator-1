from edit_text import find_all

string = '3 70 000 00 00 0ОТХОДЫ ПРОИЗВОДСТВА МАШИН И ОБОРУДОВАНИЯ3 71 000 00 00 0   Отходы производства компьютеров, \
электронных и оптических изделий3 71  100 00 00 0Отходы производства элементов электронной аппаратуры и печатных схем(плат)\
3 71  110 00 00 0Отходы производства элементов электронной аппаратуры3 71  112 00 00 0Отходы производства диодов, транзисторов \
и прочих полупроводниковых приборов, включая светоизлучающие диоды, пьезоэлектрические приборы и их части7 39 000 00 00 0Отходы \
при предоставлении прочих видов услуг населению7 39 100 00 00 0Отходы при оказании услуг \
по захоронению коммунальных отходов7 39 101 00 00 0Инфилътрационные воды объектов размещения твердых коммунальныхотходов7 \
39 101  11  39 3фильтрат полигонов захоронения твердых коммунальных отходов умеренно опасный7 39 101  12 39 4фильтрат полигонов \
захоронения твердых коммунальных отходов малоопасный7 39 102 00 00 0Отходы дезинфекции колес мусоровозов7 39 102 1129 4опилки, \
пропитанные вироцидом, отработанные7 39 102 12 29 4опилки, пропитанные лизолом, отработанные7 39 102 13 29 4опилки, обработанные \
хлорсодержащими дезинфицирующими средствами, отработанные7 39 102 21 29 4опилки, обработанные гуанидинсодержащими дезинфицирующими \
средствами, отработанные7 39 103 00 00 0Отходы при обслуживании сооружений для сбора и отводаинфильтрационных вод объектов захоронения \
твердых коммунальныхотходов7 39 103  11  39 4отходы очистки дренажных канав, прудов-накопителей фильтрата полигонов захоронения твердых\
 коммунальных отходов малоопасные7 39 311  01  72 5отходы (мусор) от уборки помещений нежилых религиозных зданий7 39 400 00 00 0Отходы \
 при предоставлении услуг парикмахерскими, салонамикрасоты, соляриями, банями, саунами, относящиеся к  твердымкоммунальным отходам7 39 \
 410 00 00 0Отходы (мусор) от уборки парикмахерских,  салонов красоты,  соляриев7 39 410 01 72 4отходы (мусор) от уборки помещений \
 парикмахерских, салонов красоты, соляриев7 39 411 31 72 4отходы ватных дисков, палочек, салфеток с остатками косметических средств7 \
 39413  11 29 5отходы волос7 39 420 00 00 0Отходы  (мусор) от уборки бань,  саун,  прачечных7 39 421  01 72 5отходы от уборки бань, \
 саун7 39 422 11 72 4отходы от уборки бань, саун, содержащие остатки моющих средств7 39 500 00 00 0Отходы при стирке и чистке одежды, \
 т екст ильных и меховых изделий7 39 511 01 29 4отходы (ворс) очистки фильтров сушильных машин при чистке хлопчатобумажных текстильных \
 изделий7 39 515  11 49 5отходы зачистки гладильного, сушильного оборудования73951801  394отходы зачистки виброфильтров предварительной \
 очистки сточных вод стирки и чистки текстильных издели'


def hierarchy():
    list = find_all(string)
    list = list[:-2]
    first_lvl = '00 000 00 00 0'
    second_lvl = '0 000 00 00 0'
    third_lvl = '000 00 00 0'
    fourth_lvl = '00 00 00 0'
    fifth_lvl = '0 00 00 0'
    bla = '00 00 0'
    for nested_list in list:
        if first_lvl in nested_list[0]:
            print('First level:', nested_list)
        elif second_lvl in nested_list[0]:
            print('Second level:', nested_list)
        elif third_lvl in nested_list[0]:
            print('Third level:', nested_list)
        elif fourth_lvl in nested_list[0]:
            print('Fourth level:', nested_list)
        elif fifth_lvl in nested_list[0]:
            print('Fifth level:', nested_list)
        elif bla in nested_list[0]:
            print('Bla:', nested_list)
        else:
            print(nested_list)

hierarchy()

