import xml.etree.ElementTree as ET

root = ET.parse('BrazilInstance1.xml')
#root = ET.parse('ItalyInstance1.xml')

class Constraint:

    tagConstraints = []
    idEventGroup = []
    idConstraints = []
    referenceResourceType = []
    referenceResourceGroup = []
    teste = []

    def __init__(self, path, dictConstraint):
        self.path = path
        self.dictConstraint = dictConstraint
        self.appliesto = []
        self.timegroup = []

    def get_constraint(self):

        for xml in root.findall('./Instances/Instance/Constraints'):
            tagConstraints.append(xml.tag)

        y = 0
        time = []
        z = 0
        for xml in root.findall('./Instances/Instance/Constraints/'):
            x = 0
            teste.append(xml.attrib.get('Id'))
            resto_dict = {}
            while x < len(xml):
                resto_dict[xml[x].tag] = xml[x].text

                if xml[x].tag == 'AppliesTo':
                    for z  in range(len(xml[4][0])):
                        self.appliesto.append(xml[4][0][z].attrib.get('Reference'))

                        #z += 1
                    resto_dict[xml[x].tag] = self.appliesto
                if xml[x].tag == 'TimeGroups':
                    # print(len(xml[x]))
                    # print(xml[x][0].attrib.get('Reference'))
                    for z in range(len(xml[x])):
                        self.timegroup.append(xml[x][z].attrib.get('Reference'))

                        #z += 1
                    resto_dict[xml[x].tag] = self.timegroup
                if xml[x].tag == 'Times':
                    # print(len(xml[x]))
                    # print(xml[x][0].attrib.get('Reference'))
                    for z in range(len(xml[x])):
                        time.append(xml[x][z].attrib.get('Reference'))

                        #z += 1
                    resto_dict[xml[x].tag] = time
                self.dictConstraint[teste[y]] = resto_dict
                self.appliesto = []
                self.timegroup = []
                time = []
                x += 1
            y += 1
        #print(x)
        for xml in root.findall('./Instances/Instance/Events/EventGroups/EventGroup'):
            idEventGroup.append(xml.attrib.get('Id'))


        return self.dictConstraint


    def print_constraint(self):

        print(f'dicionario com as restricoes {self.dictConstraint}\n')
        print(len(self.dictConstraint))
        print(self.appliesto)
        print(self.timegroup)


    def __str__(self):
        return f'{self.dictConstraint}'

constraint = Constraint(root, dictConstraint={})
dic = constraint.get_constraint()
print(constraint)

