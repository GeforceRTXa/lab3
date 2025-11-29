from src.constants import BANWORDS
from src.sorts import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort # noqa: F401
from src.stack import LinkedList

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    node_mode = False
    linked_list = LinkedList()
    while True:
        try:
            command = input("Введите вашу команду: ")
            if command == "node_mode":
                print("Your mode is now node_mode")
                node_mode = True
                continue
            if node_mode:
                s = command.split()
                if len(s) == 0:
                    raise SyntaxError
                if s[0] == "pop":
                    if len(s) > 1:
                        raise SyntaxError
                    print(linked_list.pop())
                elif s[0] == "len":
                    if len(s) > 1:
                        raise SyntaxError
                    print(len(linked_list))
                elif s[0] == "peek":
                    if len(s) > 1:
                        raise SyntaxError
                    print(linked_list.peek())
                elif s[0] == "min":
                    if len(s) > 1:
                        raise SyntaxError
                    print(linked_list.min())
                elif s[0] == "is_empty":
                    if len(s) > 1:
                        raise SyntaxError
                    print(linked_list.is_empty())
                elif s[0] == "sort_mode":
                    if len(s) > 1:
                        raise SyntaxError
                    linked_list = LinkedList()
                    print("Your mode now is sort_mode")
                    node_mode = False
                    continue
                elif s[0] == "push":
                    if len(s) != 2:
                        raise SyntaxError
                    value = s[1]
                    try:
                        if "." in value:
                            value_for_list = float(value)
                        else:
                            value_for_list = int(value)
                        linked_list.push(value_for_list)
                    except TypeError:
                        raise SyntaxError
                else:
                    raise SyntaxError
            else:
                for i in BANWORDS:
                    if i in command:
                        raise Exception("Your command has banned word")
                print(eval(command))
        except SyntaxError:
            print("Invalid syntax")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
