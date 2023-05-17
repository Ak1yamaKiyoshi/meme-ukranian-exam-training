accents = """\nагронОмія\nалфАвІт\nАркушик\nасиметрІя\nбагаторазОвий\nбезпринцИпний\nбЕшкет\nблАговіст\nблизькИй\nболотИстий\nборОдавка\nбосОніж\nбоЯзнь\nбурштинОвий\nбюлетЕнь\nвАги (у множині)\nвантажІвка\nвеснЯнИй\nвИгода (користь)\nвигОда (зручність)\nвидАння\nвизвОльний\nвимОга\nвИпадок\nвирАзний\nвИсіти\nвИтрата\nвишИваний\nвідвезтИ\nвідвестИ\nвІдгомін\nвіднестИ\nвІдомість (список)\nвідОмість (повідомлення, дані, популярність)\nвІрші\nвіршовИй\nвітчИм\nгальмО\nгАльма\nглядАч\nгорошИна\nграблІ\nгуртОжиток\nданИна\nдАно\nдецимЕтр\nдЕщиця\nде-Юре\nджерелО\nдИвлячись\nдичАвіти\nдіалОг\nдобовИй\nдобУток\nдовезтИ\nдовестИ\nдовІдник\nдОгмат\nдонестИ\nдОнька\nдочкА\nдрОва\nекспЕрт\nєретИк\nжалюзІ\nзавдАння\nзавезтИ\nзавестИ\nзАвжди\nзавчасУ\nзАгадка\nзаіржАвілий\nзаіржАвіти\nзакінчИти\nзАкладка (у книзі)\nзАкрутка\nзалишИти\nзамІжня\nзанестИ\nзАпонка\nзаробІток\nзАставка\nзАстібка\nзастОпорити\nзвИсока\nздАлека\nзібрАння\nзобразИти\nзОзла\nзрАння\nзрУчний\nзубОжіння\nіндУстрія\nкАмбала\nкаталОг\nквартАл\nкИшка\nкіломЕтр\nкінчИти\nкОлесо\nкОлія\nкОпчений (дієприкметник)\nкопчЕний (прикметник)\nкорИсний\nкОсий\nкотрИй\nкрицЕвий\nкрОїти\nкропивА\nкулінАрія\nкУрятина\nлАте\nлистопАд\nлітОпис\nлЮстро\nмАбУть\nмагістЕрський\nмАркетинг\nмерЕжа\nметалУргія\nмілімЕтр\nнавчАння\nнанестИ\nнапІй\nнАскрізний\nнАчинка\nненАвидіти\nненАвисний\nненАвисть\nнестИ\nнІздря\nновИй\nобіцЯнка\nобрАння\nобрУч (іменник)\nодинАдцять\nодноразОвий\nознАка\nОлень\nоптОвий\nосетЕр\nотАман\nОцет\nпавИч\nпартЕр\nпЕкарський\nперевезтИ\nперевестИ\nперЕкис\nперелЯк\nперенестИ\nперЕпад\nперЕпис\nпіалА\nпІдданий (дієприкметник)\nпіддАний (іменник, істота)\nпІдлітковий\nпізнАння\nпітнИй\nпіцЕрія\nпОдруга\nпОзначка\nпОмилка\nпомІщик\nпомОвчати\nпонЯття\nпорядкОвий\nпосерЕдині\nпривезтИ\nпривестИ\nпрИморозок\nпринестИ\nпрИчіп\nпрОділ\nпромІжок\nпсевдонІм\nрАзом\nрЕмінь (пояс)\nрЕшето\nрИнковий\nрівнИна\nроздрібнИй\nрОзпірка\nрукОпис\nруслО\nсантимЕтр\nсвЕрдло\nсерЕдина\nсЕча\nсиметрІя\nсільськогосподАрський\nсімдесЯт\nслИна\nсоломИнка\nстАтуя\nстовідсОтковий\nстрибАти\nтекстовИй\nтечіЯ\nтИгровий\nтисОвий\nтім’янИй\nтравестІя\nтризУб\nтУлуб\nукраЇнський\nуподОбання\nурочИстий\nусерЕдині\nфартУх\nфаховИй\nфенОмен\nфОльга\nфОрзац\nхАос (у міфології: стихія)\nхаОс (безлад)\nцАрина\nцемЕнт\nцЕнтнер\nціннИк\nчарівнИй\nчерговИй\nчитАння\nчорнОзем\nчорнОслив\nчотирнАдцять\nшляхопровІд\nшовкОвий\nшофЕр\nщЕлепа\nщИпці\nщодобовИй"""

PURPLE =   '\033[95m'
BLUE =     '\033[94m'
CYAN =     '\033[96m'
GREEN =    '\033[92m'
YELLOW =   '\033[93m'
RED =      '\033[91m'
NORMAL =   '\033[0m'
BOLD =     '\033[1m'
UNDERLINE ='\033[4m'
    
def findDifference(str1, str2):    
    """str1 - correct, str2 - incorrect """
    
    output = ""
    for i in range(max(len(str1), len(str2))):
        try: str1[i]
        except: continue
        try: str2[i]
        except: 
            output += YELLOW + BOLD + str1[i]
            continue
        if str1[i] == str2[i]: output += GREEN + BOLD + str1[i];
        else: output += RED + BOLD + str1[i]
    return output    
    
    
def quiz(accents):
    """ start quiz """
    
    # Greeting message with instructions 
    print(NORMAL + BOLD + '\n' + '~ ~ Невеличкий скрипт для перевірки наголосів для НМТ :). \n > мій гітхаб: https://github.com/Ak1yamaKiyoshi'
        + RED    + '\n' + " > введіть 'ЗУПИНИТИСЬ' щоб зупинитись і побачити результати "
        + YELLOW + '\n' + " > Вам потрібно вводити слова позначаючи наголос великою літерою: алфАвІт"
        + GREEN  + '\n' + ' > Поточне слово -> слово без позначеного наголосу \n      [000/231]  ->  алфавіт '
        + NORMAL + UNDERLINE + BOLD + '\n > Успіхів! ' + NORMAL)

    state = {
        "correct":0,             # correct user answers 
        "incorrect":0,           # incorrect user answers 
        "skipped":0,             # skiped by user answers 
        "errors_highlighted":[], # array of incorrect answers with error highlighting 
        "errors":[],             # array of incorrect answers without error highlighting
        "stop_word":"ЗУПИНИТИСЬ" # word to skip all following tests, and end the test
    }
    
    # calculate quiz length 
    quiz_length = len(set(accents.split("\n")))
    for index, string in enumerate(set(accents.split("\n"))):
        # if there is string with description 
        # cut all, that not belong to the accent 
        # example: "вИгода (користь)"" -> "вИгода"
        correct_answer = string[:string.find("(")].strip() if "(" in string else string.strip()
        
        # avoid empty quizez
        if len(string.strip()) == 0: continue

        # Message with test counter and question 
        print("" + NORMAL 
            + BLUE + f"[{index+1}/{quiz_length}]" # counter [current/total]
            + NORMAL + " -> "
            + YELLOW + BOLD + UNDERLINE + f"{string.lower()}" # question; word
        )
        
        # Ask user to input answer
        user_answer = input(NORMAL + f"Позначте наголос: " + BOLD + CYAN).strip();
        # check, if answer is correct; if so, update state
        if user_answer == correct_answer: state["correct"] += 1
        # check, if answer is skipped; if so, update the state 
        elif user_answer == "": state["skipped"] += 1
        # check, if user entered stop word; if so, update skipped counter and break cycle
        elif user_answer == state['stop_word']: state['skipped'] += (quiz_length - index); break
        # if answer is incorrect
        else: 
            # append error ( to use as questions in next quiz, based on errors in current )
            state['errors'].append(string)
            # update state incorrect counter
            state['incorrect'] += 1 
            # find errors in user answers
            error = findDifference( correct_answer, user_answer ) 
            # ouput user error
            print('\033[0m' + f" > {error}") 
            # append highlighted errors ( to display after results )
            state["errors_highlighted"].append(error) 
        
    # Results message
    print(""    + BOLD
        +         PURPLE + "__________________"
        + '\n'  + GREEN  + "Правильно   ->  " + f"{state['correct']}"
        + '\n'  + RED    + "Неправильно ->  " + f"{state['incorrect']}"
        + '\n'  + YELLOW + "Разом       ->  " + f"{state['correct'] + state['incorrect']}"
        + '\n'  + BLUE   + "Пропущено   ->  " + f"{state['skipped']}"
        )

    # Print Errors Message
    if input( NORMAL + BOLD + "Вивести помилки? так/ні: " + CYAN) == "так":
        # sort errors 
        state['errors_highlighted'] = sorted(state['errors_highlighted'])
        # Empty accents to write new questions to it  
        accents = "" 
        for i in range(len(state['errors_highlighted'])):
            # print error with number
            print(NORMAL + BOLD + BLUE + f"[{i+1}/{state['incorrect']}]: {state['errors_highlighted'][i]}")
            # append errors (not highlighted) to accent 
            accents += state['errors'][i] + "\n" 
        # delete first "\n"
    
    # if restart, recursive call using new errors
    if input( NORMAL + BOLD + "Перепройти з виправленням помилок? так/ні " + CYAN) == "так":    
        quiz(accents) 
    else:
        input(YELLOW + "Натисніть Enter щоб закрити консоль " + NORMAL)

quiz(accents)