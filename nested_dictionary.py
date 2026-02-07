student_database = {
    'Student1':{
        'prénom':'Aayan',
        'surname':'ismail',
        'age':'fifteen',
        'marks':{
            'maths':98,
            'english':90,
            'irish':65,
            'latin':95,
            'german':73,
            'french':70,
            'science':90
        }

    },
    'student2':{
        'prénom':'hugh',
        'surname':'cunnigham',
        'age':'fifteen',
        'marks':{
            'maths':60,
            'english':50,
            'irish':90,
            'geography':25,
            'art':50
        }

      },
      'student3':{
          'prénom':'klein',
          'surname':'mingrui',
          'age':'unknown',
          'marks':{
              'ancient_feysac':98,
              'ancient_hermes':96,
              'elvish':92,
              'hermes':90,
              'jotun':88,
              'mandarin':100,
              'english':60
          }
      },
      'student4':{
          'prénom':'johan',
          'surname':'liebert',
          'age':'unknown',
          'marks':{
              'latin':99,
              'french':100,
              'german':98,
              'english':97,
              'czech':96,
              'law':100,
              'psychology':100,
              'philosophy':100
          }

      },
      'student5':{
          'prénom':'sasaki',
          'surname':'kaneki',
          'age':'25',
          'marks':{
              'english':100,
              'masochism':100,
              'torture':100,
              'ghoul':100
          }
      }

}

for student_id, student_data in student_database.items():
    print('\nstudentid:', student_id)
    print('first name:', student_data['prénom'])
    print('surname', student_data['surname'])
    print('age:', student_data['age'])
    print('marks:')
    for subject, score in student_data['marks'].items():
        print('', subject, ':', score)

for student_data in student_database.values():
    student_data['marks']['english'] += 5

print('\nupdated the marks of english')
for student_id, student_data in student_database.items():
    print(student_id, '-', student_data['marks']['english'])