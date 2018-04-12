# 基于 python3 实现的链表数组

## 使用方式

### 创建

`linked_list = SingleLinkedList()`

### 方法

* is_empty() 判断链表是否为空，True 不为空；False 为空
* length() 返回链表长度
* appent(item) 在链表首位插入节点，其中：item 为节点元素
* add(item) 在链表末尾插入节点，其中：item 为节点元素
* travel() 遍历链表中各节点的元素
* insert(pos, item) 在指定索引处插入元素，其中：pos 为插入索引；item 为阶段元素
* remove(item) 移除与 item 相同的第一次出现的元素，如果删除成功返回提示字符串，否则返回 None，其中：item 为需要删除的元素
* search(item) 查询与 item 相同的第一次出现的元素位置并返回，若链表中不存在相同的元素，则返回 None，其中，Item 为需要查询的元素