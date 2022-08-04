



# to load values to widgets;
lblRightframe_countPeople.config(text=str(self.count))
etrRightframe_countPeople.config(text=str(self.count))




# howto insert values to entry widgets
etrRightframe_countPeople.delete(0, END)
etrRightframe_countPeople.insert(END, str(self.count))