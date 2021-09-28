import xml.etree.ElementTree as ET      #library used to parse xml
import re                               # library used to split the message tag to obtain eid value

tree = ET.parse('Exercise1/ExerciseXML.xml')
root = tree.getroot()

# a function to search for the tag in xml and return text
def getTagValue(parent, searchTag):
    tagValue = ''
    for child in parent:
        if searchTag in child.tag:
            return child.text
        else:
            # print(child.tag)
            tagValue = getTagValue(child, searchTag)
            if tagValue != '':
                break

    return tagValue


# getting the text of the required tags
transactionId = getTagValue(root, '}RelatesTo')
transactionId = transactionId.split('/')[3]

subjectCode = getTagValue(root, '}Subject')
reasonCode = getTagValue(root, '}Reason')
processingStart = getTagValue(root, '}ProcessingStart')
processingEnd = getTagValue(root, '}ProcessingEnd')
status = getTagValue(root, '}Status')

message = getTagValue(root[1], '}Message')
message = re.split(' - |\. ', message)
message = dict(item.split(":") for item in message)


# writing the result to a text file
f = open("Exercise1/Output1.txt", "a")
f.write('TransactionID ' + transactionId)
f.write('\nSubjectCode ' + subjectCode)
f.write('\nReasonCode ' + reasonCode)
f.write('\nProcessingStart ' + processingStart)
f.write('\nProcessingEnd ' + processingEnd)
f.write('\nStatus ' + status)
f.write('\nEID ' + message.pop('eid'))

f.close()

# f.write('\nSubjectCode ' + root[1][0][3][1][0].text)
