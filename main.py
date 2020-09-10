# Author: Shang Yuan Lim szl6038@psu.edu
# Collaborator: Yong Lin Kwang yqk5211@psu.edu
# Collaborator: Sean Murphy spm6407@psu.edu
# Section: 010R
# Breakout: 2

def getCourseGrade(GradePoints):
  if GradePoints>=93.0:
    letter = "A"
  elif GradePoints>=90.0:
    letter = "A-"
  elif GradePoints>=87.0:
    letter = "B+"
  elif GradePoints>=83.0:
    letter = "B"
  elif GradePoints>=80.0:
    letter = "B-"
  elif GradePoints>=77.0:
    letter = "C+"
  elif GradePoints>=70.0:
    letter = "C"
  elif GradePoints>=60.0:
    letter = "D"
  else:
    letter = "F"

  return letter

def run():
  percent = input("Enter your CMPSC 131 grade: ")

  percent = float(percent)

  grade = getCourseGrade(percent)

  print(f"Your letter grade for CMPSC 131 is {grade}.")

if __name__ == "__main__":
  run() 
