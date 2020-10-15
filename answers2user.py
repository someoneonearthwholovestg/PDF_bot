# available languages
ENG, RUS = "eng", "rus"

HELP = "help"
CHANGE_LANGUAGE = "change_language"
CANCEL_CREATE_PDF = "cancel"
ENTER_FILENAME = "enter_filename"
CORRECT_FILENAME = "correct_filename"
SEND_AMOUNT_PHOTO = "send_amount_photo"
CORRECT_AMOUNT_PHOTO = ""
SEND_PHOTO = "send_photo"
ADD_or_END = "add_or_end"
ADD_PHOTO = "add_photo"
WAIT_TIME = "wait_time"
BYE = "bye"

answers = {
            HELP: {ENG: "This bot creates a PDF file from the photos you send to it.\n\n"
                        "Take a look at the commands currently available:\n\n"
                        "/create_pdf - the main command that creates the PDF file\n"
                        "/change_language - switch language\n",

                   RUS: "ഈ ബോട്ട് നിങ്ങൾ അയച്ച ഫോട്ടോകളിൽ നിന്ന് ഒരു PDF ഫയൽ സൃഷ്ടിക്കുന്നു..\n\n"
                        "നിലവിൽ ലഭ്യമായ കമാൻഡുകൾ പരിശോധിക്കുക:\n\n"
                        "/create_pdf - PDF ഫയൽ സൃഷ്ടിക്കുന്ന പ്രധാന കമാൻഡ്\n"
                        "/change_language - ഭാഷ മാറ്റുക\n",},

            CHANGE_LANGUAGE: {ENG: "Language changed to English!\n",
                              RUS: "Язык сменен на русский!\n"},

            CANCEL_CREATE_PDF: {ENG: "If you change your mind about creating a PDF file, send me /cancel.\n",
                                RUS: "Если вы передумали создавать PDF файл, то введите команду /cancel.\n"},

            ENTER_FILENAME: {ENG: "Enter filename (without extension) please!\n",
                             RUS: "Введите имя файла (без расширения), пожалуйста!\n"},

            CORRECT_FILENAME: {ENG: "Enter the correct filename please!\n",
                               RUS: "Введите корректное название файла, пожалуйста!\n"},

            SEND_AMOUNT_PHOTO: {ENG: "Send me the number of photos please!\n",
                                RUS: "Пришлите мне количество фотографий, пожалуйста!\n"},

            CORRECT_AMOUNT_PHOTO: {ENG: "Enter the correct number of photos please!\n",
                                   RUS: "Введите корректное значение числа фотографий, пожалуйста!\n"},

            SEND_PHOTO: {ENG: "Send me photos please!\n",
                         RUS: "Пришлите мне фотографии, пожалуйста!\n"},

            ADD_or_END: {ENG: "All photos added to your PDF file!\n"
                              "If you want to add another photos, send me /add, otherwise, /end.\n",
                         RUS: "Все фотографии добавлены в ваш PDF файл!\n"
                              "Если вы хотите добавить другие фотографии, пришлите /add, иначе /end.\n"},

            ADD_PHOTO: {ENG: "Ok, send me amount of photo, which need to add!\n",
                        RUS: "Хорошо, пришлите мне количество фотографий, которые нужно добавить!\n"},

            WAIT_TIME: {ENG: "Please, wait some time!\n",
                        RUS: "Пожалуйста, подождите некоторое время!\n"},

            BYE: {ENG: "Thank you for using me! See you again!\n",
                  RUS: "Спасибо за использование! Увидимся!\n"}
           }
