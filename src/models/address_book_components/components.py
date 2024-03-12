import re


class Field:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)    


class Name(Field):
     def __init__(self,value):
         self.value = value


class Phone(Field):
    
    def __init__(self,value):
            self.value = value

    def validate_phone(self):
        if len(self.value) == 10:
            return self.value
        else:
            raise ValueError("Phone number must be exactly 10 digits")   

class Birthday(Field):
      def __init__(self,value):
          self.value = value    
      
      def validateDate(self):
          date_pattern = r'\d{1,2}\.\d{1,2}\.\d{4}'

          if not re.match(date_pattern, self.value):
              raise ValueError("Date birthday must be in format by DD.MM.YYYY")    