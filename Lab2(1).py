def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    cal_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g.5,67,32)")

def get_user_input():
    x = input()
    print(x)
    y = x.split(",")
    print(y)
    i = []
    for z in y:
        i.append(float(z))
    return(i)

def cal_average(num_list):
    avg = sum(num_list)/len(num_list)
    print(avg)

def find_min_max(num_list):
    minmax = [min(num_list), max(num_list)]
    print(minmax)

def sort_temperature(num_list):
    num_list.sort()
    print(num_list)

def calc_median_temperature(num_list):
    no = len(num_list)
    num_list.sort()
    if no % 2 == 0:
        median1 = num_list[no//2]
        median2 = num_list[no // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = num_list[no // 2]
    print("The median of the given numbers  (", num_list, ") is", str(median))

if __name__ == "__main__":
    main()