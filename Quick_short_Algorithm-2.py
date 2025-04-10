#!/usr/bin/env python
# coding: utf-8

# In[10]:


import time
import timeit
import random
import matplotlib.pyplot as plt


# In[11]:


def generate_data(size):
    data = [random.randint(0, 1000) for _ in range(size)]
    return data


# In[12]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# In[13]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# In[14]:


def analyze_sorting_time(data_sizes):
    sorting_times = []
    for size in data_sizes:
        data = generate_data(size)
        start_time = time.time()
        bubble_sort(data)
        end_time = time.time()
        sorting_time = end_time - start_time
        sorting_times.append(sorting_time)
    return sorting_times


# In[15]:


def analyze_search_time(data_sizes, search_size):
    search_times = []
    for size in data_sizes:
        data = generate_data(size)
        data.sort()  
        search_element = random.choice(data[:search_size])
        start_time = time.time()
        binary_search(data, search_element)
        end_time = time.time()
        search_time = end_time - start_time
        search_times.append(search_time)
    return search_times


# In[16]:


def plot_analysis(data_sizes, sorting_times, search_times):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(data_sizes, sorting_times, marker='o', linestyle='-')
    plt.title('Sorting Time Analysis')
    plt.xlabel('Data Size')
    plt.ylabel('Time (s)')

    plt.subplot(1, 2, 2)
    plt.plot(data_sizes, search_times, marker='o', linestyle='-')
    plt.title('Binary Search Time Analysis')
    plt.xlabel('Data Size')
    plt.ylabel('Time (s)')

    plt.tight_layout()
    plt.show()


# In[17]:


if __name__ == "__main__":
    data_sizes = [50, 100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]  
    sorting_times = analyze_sorting_time(data_sizes)
    search_times = analyze_search_time(data_sizes, search_size=50)
    plot_analysis(data_sizes, sorting_times, search_times)


# In[18]:


def generate_data(size):
    data = [random.randint(1, 30000) for _ in range(size)]
    return data

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

def analyze_time_efficiency():
    data_size = 30000  
    data = generate_data(data_size)
    
    sort_time = timeit.timeit(lambda: quicksort(data.copy()), number=1)
    
    target = random.choice(data)
    data.sort() 
    search_time = timeit.timeit(lambda: binary_search(data, target), number=1)
    
    print(f"Data Size: {data_size}")
    print(f"Time taken for sorting: {sort_time:.10f} seconds")
    print(f"Time taken for binary search: {search_time:.10f} seconds")

if __name__ == "__main__":
    analyze_time_efficiency()


# In[ ]:




