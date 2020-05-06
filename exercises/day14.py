with open("./files/iris.csv", "w") as iris_file:
    iris_file.write(
        """sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5,3.6,1.4,0.2,Iris-setosa
7,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
6.9,3.1,4.9,1.5,Iris-versicolor
5.5,2.3,4,1.3,Iris-versicolor
6.5,2.8,4.6,1.5,Iris-versicolor
6.3,3.3,6,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
7.1,3,5.9,2.1,Iris-virginica
6.3,2.9,5.6,1.8,Iris-virginica
6.5,3,5.8,2.2,Iris-virginica"""
    )

with open("./files/iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

#creating a list of dictionaries
irises = []
headers = iris_data[0].strip().split(",")

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))
    irises.append(iris_dict)

#going back to csv
for iris in irises:
    print(",".join(iris.values()))