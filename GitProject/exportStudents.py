class ExportStudents:
    @staticmethod
    def csv(path, list):
        file = open(path, "w")

        lines = []

        for i in range(1, len(list)):
            student_details = list[i]
            line = []

            for student_detail_key in student_details:
                line.append(student_details[student_detail_key])

            line = ";".join(line)

            if i < len(list) - 1:
                line += "\n"

            lines.append(line)

        file.writelines(lines)

    @staticmethod
    def txt(path, list):
        file = open(path, "w")

        lines = []

        for i in range(1, len(list)):
            student_details = list[i]

            line = []

            for student_detail_key in student_details:
                line.append(student_details[student_detail_key])

                if student_detail_key == "Surname":
                    line.append(" - ")
                else:
                    line.append(" ")


            line.pop()

            line = "".join(line)

            if i < len(list) - 1:
                line += "\n"

            lines.append(line)

        file.writelines(lines)