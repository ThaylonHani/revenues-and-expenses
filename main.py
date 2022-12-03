import os


def Main():
    os.system("clear") or None
    expenses_list = []
    revenues_list = []
    revenues = 0
    expenses = 0
    print("--------Bem vindo ao seeExpenses--------")
    print("#######################################")
    print("### Aqui você vê a sua renda mensal ###")
    print("#######################################")
    print("Subtraímos a suas receitas com despesas")
    print("")
    print("Qual serviço usar ?")
    print("(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
    revenue_or_expenses = input("Número da opção: ")

    while (revenue_or_expenses != "6"):
        os.system("clear") or None
        if (revenue_or_expenses == "1"):
            revenues_list = []
            revenue_input = float(input("Adicionar receita: "))
            revenues_list.append(revenue_input)
            for i in revenues_list:
                revenues += i
                os.system("clear") or None
                print(
                    "(1) informar mais uma receita\n(2) Voltar para o menu\n(3) Total de receitas")
                recipe_selection_session = input("Opção: ")
                if (recipe_selection_session == "1"):
                    os.system("clear") or None
                    revenue_input = float(input("Adicionar receita: "))
                    revenues_list.append(revenue_input)
                elif (recipe_selection_session == "2"):
                    os.system("clear") or None
                    print(
                        "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                    revenue_or_expenses = input("Número da opção: ")

                elif (recipe_selection_session == "3"):
                    os.system("clear") or None
                    print("As receitas são igual a: {:05.2f}".format(
                        revenues), "$")
                    print("(1) informar mais uma receita\n(2) Voltar para o menu")
                    total_choice_session = input("Opção: ")
                    if (total_choice_session) == "1":
                        os.system("clear") or None
                        revenue_input = float(input("Receita: "))
                        revenues_list.append(revenue_input)
                    elif (total_choice_session == "2"):
                        os.system("clear") or None
                        print(
                            "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                        revenue_or_expenses = input("Número da opção: ")

                    else:
                        print("Opção inválida")
                        print("(1) informar mais uma receita\n(2) Voltar para o menu")
                        total_choice_session = input("Opção: ")

        elif (revenue_or_expenses == "2"):
            expenses_list = []
            expenses_input = float(input("Adicionar despesa: "))
            expenses_list.append(expenses_input)
            for i in expenses_list:
                expenses += i
                os.system("clear") or None
                print(
                    "(1) informar mais uma despesa\n(2) Voltar para o menu\n(3) Total de despesas")
                recipe_selection_session = input("Opção: ")
                if (recipe_selection_session == "1"):
                    os.system("clear") or None
                    expenses_input = float(input("Adicionar despesa: "))
                    expenses_list.append(expenses_input)
                elif (recipe_selection_session == "2"):
                    os.system("clear") or None
                    print(
                        "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                    revenue_or_expenses = input("Número da opção: ")

                elif (recipe_selection_session == "3"):
                    os.system("clear") or None
                    print("As despesas são igual a: {:05.2f}".format(
                        expenses), "$")
                    print("(1) informar mais uma despesa\n(2) Voltar para o menu")
                    total_choice_session = input("Opção: ")
                    if (total_choice_session == "1"):
                        os.system("clear") or None
                        expenses_input = float(input("Despesa: "))
                        expenses_list.append(expenses_input)
                    elif (total_choice_session == "2"):
                        os.system("clear") or None
                        print(
                            "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                        revenue_or_expenses = input("Número da opção: ")

                    else:
                        print("Opção inválida")
                        print("(1) informar mais uma despesa\n(2) Voltar para o menu")
                        total_choice_session = input("Opção: ")

        elif (revenue_or_expenses == "3"):
            os.system("clear") or None
            print("Despesas: {:05.2f}".format(expenses))
            print("Receitas: {:05.2f}".format(revenues))
            calc = revenues - expenses
            if(calc < 0 ):
                print(
                "A diferença entre as despesas e as receitas é de: {:05.2f}".format(calc))
                print("---Você está devendo---")
                print("")
                print("Qual serviço usar ?")
                print(
                "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                revenue_or_expenses = input("Número da opção: ")
            else:
                print(
                "A diferença entre as despesas e as receitas é de: {:05.2f}".format(calc))
            print("")
            print("Qual serviço usar ?")
            print(
                "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
            revenue_or_expenses = input("Número da opção: ")
                

        elif (revenue_or_expenses == "4"):
            if (revenues):
                revenues = 0
                print("--------Receitas excluídas--------")
                print("")
                print(
                    "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                revenue_or_expenses = input("Número da opção: ")
            else:
                print("---------------Não há receitas para excluir--------------")
                print("")
                print(
                    "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                revenue_or_expenses = input("Número da opção: ")

        elif (revenue_or_expenses == "5"):
            if (expenses):
                expenses = 0
                print("--------despesas excluídas--------")
                print("")
                print(
                    "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                revenue_or_expenses = input("Número da opção: ")
            else:
                print("---------------Não há despesas para excluir--------------")
                print("")
                print(
                    "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
                revenue_or_expenses = input("Número da opção: ")
        else:
            os.system("clear") or None
            print("Opção inválida")
            print("Qual serviço usar ?")
            print(
                "(1) Acrescentar receitas\n(2) Acrescentar despesas\n(3) Calcular\n(4) Limpar receitas\n(5) Limpar despesa\n(6) Sair")
            revenue_or_expenses = input("Número da opção: ")

    print("----------------------------------")
    print("------------- OBRIGADO -----------")
    print("--------------- POR --------------")
    print("--------------- Usar -------------")
    print("----------- seeExpenses ----------")
    print("----------------------------------")


if(__name__ == "__main__"):
    Main()