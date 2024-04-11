import math
from Student import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(a):
        return a.head ==None
    def traverse(a):
        pt = a.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")
    def clear(self):
        self.head = None

    def addStudentLast(self, student):
        if not self.head:
            self.head = Node(student)
            self.tail = self.head
        else:
            current = self.head
            while current:
                if current.data.Id == student.Id:
                    print("Student ID already exists.")
                    return
                current = current.next

            new_node = Node(student)
            self.tail.next = new_node
            self.tail = new_node

    def addStudentHead(self, student):
        new_node = Node(student)  # Create a new node with the student data

        if not self.head:
            # If the linked list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Set the next pointer of the new node to the current head
            new_node.next = self.head
            # Update the head to the new node
            self.head = new_node
    def findStudentById(self, student_id):
        current = self.head
        while current:
            if current.data.Id == student_id:
                return current.data
            current = current.next
        return None

    def updateStudent(self, student_id, updated_student):
        current = self.head
        while current:
            if current.data.Id == student_id:
                current.data.Name = updated_student.Name
                current.data.Address = updated_student.Address
                current.data.Score = updated_student.Score
                return True
            current = current.next
        return False

    def deleteStudent(self, student_id):
        if not self.head:
            return False

        if self.head.data.Id == student_id:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        current = self.head
        while current.next:
            if current.next.data.Id == student_id:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next

        return False

    def deleteStudentAfter(self, student_id):
        if not self.head:
            return False

        current = self.head
        while current.next:
            if current.data.Id == student_id:
                # Check if the next node exists
                if current.next:
                    current.next = current.next.next
                    if current.next is None:
                        # If the next node is None, update the tail
                        self.tail = current
                    return True
            current = current.next

        return False

    def deleteStudentBefore(self, student_id):
        if not self.head or not self.head.next:
            return False

        if self.head.next.data.Id == student_id:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        current = self.head
        while current.next.next:
            if current.next.next.data.Id == student_id:
                current.next = current.next.next
                return True
            current = current.next

        return False
#Xoá node có điểm la cao nhất
    def deleteStudentWithMaxScore(self):
        if not self.head:
            return False

        max_score = -1
        max_score_node = None

        current = self.head
        while current:
            if current.data.Score > max_score:
                max_score = current.data.Score
                max_score_node = current
            current = current.next

        if max_score_node:
            if max_score_node == self.head:
                self.head = self.head.next
                if not self.head:
                    self.tail = None
            else:
                prev = self.head
                while prev.next != max_score_node:
                    prev = prev.next

                prev.next = max_score_node.next
                if max_score_node == self.tail:
                    self.tail = prev
            return True

        return False

    def deleteStudentWithSecondMaxScore(self):
        if not self.head or not self.head.next:
            return False

        max_score = -1
        second_max_score = -1
        max_score_node = None
        second_max_score_node = None

        current = self.head
        while current:
            if current.data.Score > max_score:
                second_max_score = max_score
                second_max_score_node = max_score_node
                max_score = current.data.Score
                max_score_node = current
            elif current.data.Score > second_max_score and current.data.Score != max_score:
                second_max_score = current.data.Score
                second_max_score_node = current
            current = current.next

        if second_max_score_node:
            if second_max_score_node == self.head:
                self.head = self.head.next
                if not self.head:
                    self.tail = None
            else:
                prev = self.head
                while prev.next != second_max_score_node:
                    prev = prev.next

                prev.next = second_max_score_node.next
                if second_max_score_node == self.tail:
                    self.tail = prev
            return True

        return False

    def deleteStudentWithMinScore(self):
        if not self.head:
            return False

        min_score = float('inf')
        min_score_node = None

        current = self.head
        while current:
            if current.data.Score < min_score:
                min_score = current.data.Score
                min_score_node = current
            current = current.next

        if min_score_node:
            if min_score_node == self.head:
                self.head = self.head.next
                if not self.head:
                    self.tail = None
            else:
                prev = self.head
                while prev.next != min_score_node:
                    prev = prev.next

                prev.next = min_score_node.next
                if min_score_node == self.tail:
                    self.tail = prev
            return True

        return False

    def deleteStudentWithSecondMinScore(self):
        if not self.head or not self.head.next:
            return False

        min_score = float('inf')
        second_min_score = float('inf')
        min_score_node = None
        second_min_score_node = None

        current = self.head
        while current:
            if current.data.Score < min_score:
                second_min_score = min_score
                second_min_score_node = min_score_node
                min_score = current.data.Score
                min_score_node = current
            elif current.data.Score < second_min_score and current.data.Score != min_score:
                second_min_score = current.data.Score
                second_min_score_node = current
            current = current.next

        if second_min_score_node:
            if second_min_score_node == self.head:
                self.head = self.head.next
                if not self.head:
                    self.tail = None
            else:
                prev = self.head
                while prev.next != second_min_score_node:
                    prev = prev.next

                prev.next = second_min_score_node.next
                if second_min_score_node == self.tail:
                    self.tail = prev
            return True

        return False

    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end=" ")
            pt = pt.next
        print("")

    def traverse1(self):
        pt = self.head
        while pt:
            if pt.data.Score > 5:
                print(pt.data, end=" ")
            pt = pt.next
        print("")
# Sort by score
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        lst2 = []
        cur = self.head
        while cur:
            lst2.append((cur.data.Id, cur.data.Name, cur.data.Address, cur.data.Score))
            cur = cur.next

        lst2.sort(key=lambda x: x[3], reverse=True)  # Sorting in ascending order based on score

        j = 0
        cur = self.head
        while cur:
            cur.data.Id = lst2[j][0]
            cur.data.Name = lst2[j][1]
            cur.data.Address = lst2[j][2]
            cur.data.Score = lst2[j][3]
            j += 1
            cur = cur.next

    def traverse1(self):
        pt = self.head
        count = 0
        while pt:
            print(f"({pt.data.Name},{pt.data.Score})", end=" ")
            pt = pt.next
            count += 1
            if count == 3:
                break
        print("")

    def count(self):
        curr = self.head
        count = 0
        while curr:
            if curr.data.Score > 50:
                count += 1
            curr = curr.next
        return count
    def Q5(self):
        pass
