import os
def reading():
    file_path = "/usr/share/nginx/html/test/20001_access.log.20160613"
    with open(file_path, "r") as f:
        info = f.readlines()

        date = info[0].find(":", info[0].find(":") + 1) # граница для удаления незначимой информации
        ip = info[0].find("]") + 3 # граница для удаления незначимой информации

        for i in range(len(info)):
            info[i] = info[i][1: date] + " " + info[i][ip:info[i].find("=") - 1] # оттеление от незначимой информации

    return info


def writer(info_to_write):
    file_path = "/usr/share/nginx/html/result/result.txt"
    with open(file_path, "w") as r:
        for i in range(len(info_to_write)):
            for j in range(len(info_to_write[i])):
                r.write(f"<{info_to_write[i][j].replace(':', ' ')}>\t")
            r.write("\n")


def sorting(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].split() # разбиваю цельную строку по пробелам
    arr.sort(key=lambda repeats: int(repeats[2]), reverse=True) # сортировка по количеству запросов

    return arr


def repeats_counting(source, j):
    source.sort() # сортировка исходного массива для удобства удаления повторов
    counter = 0
    destination = []
    with open("/usr/share/nginx/html/result/result.txt", "r") as f:
        a = f.readlines()
        print(len(source))
        for i in range(len(source) - 1):
            if str(source[i].replace(':', ' ')) <= a[0][1:a[0].find(">")]:
                counter += 1
                if source[i] != source[i + 1]:
                    destination.append(source[i] + " " + str(counter)) # Дописываю в конечный массив количество повторов
                    counter = 0
                i += 1
            destination.append(source[len(source) - 1] + " " + str(counter + 1)) # Дописываю последний запрос

        destination = sorting(destination)

    return destination


def file_exist(n):

    i = 0
    with open("/usr/share/nginx/html/result/result.txt", "r") as f:
        a = f.readlines()
        a.sort(reverse=True)
        while i < len(n) and n[i][0].replace(':', ' ') != a[0][1:a[0].find(">")]:

            n[i] = 0
            i+=1
    return i


def main():
    index = file_exist(reading())
    print(index)
    writer(repeats_counting(reading(), index))


if __name__ == '__main__':
    main()
