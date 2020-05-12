import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path

mpl.rcParams['axes.spines.left'] = True
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True
mpl.rcParams['axes.linewidth'] = 2


# ZERO MATRIX
def zero(row, col):
    matrix = []
    for i in range(row):
        matrix.append([0] * col)
    return matrix


# IDENTITY MATRIX
def identity(row, col):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            if j == i:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


# MAIN MATRIX CLASS
class Matrix:

    def __init__(self, x=None, y=None):

        self.z = None
        self.ypoints = []
        self.ypoints_result = []
        self.zpoints = []
        self.zpoints_result = []
        self.xpoints = []
        self.xpoints_result = []
        if x is None:
            self.x = [[0]]
        else:
            self.x = x

        if y is None:
            self.y = [[0]]
        else:
            self.y = y
        self.lenx_ = len(self.x[0])
        self.leny_ = len(self.y[0])
        if self.lenx_ > 2:
            self.z = True

        self.leny = len(self.y)
        self.lenx = len(self.x)
        self.result = []
        self.result = [[0 for i in range(self.lenx_)] for j in range(self.lenx)]
        # print(self.result)
        if self.y is y:
            if self.lenx != self.leny or self.lenx_ != self.leny_:
                print("Matrices don't have the same dimensions. There might be an error.")
                # sys.exit()

    # FUNCTION TO MULTIPLY TWO MATRICES
    def mult(self, x=None, y=None):
        self.z = None
        if x is not None:
            self.x = x
            self.y = y
            self.leny = len(self.y)
            self.lenx = len(self.x)
            self.lenx_ = len(self.x[0])
            self.leny_ = len(self.y[0])
        if self.lenx_ != self.leny:
            raise ArithmeticError('Matrix A columns should match Matrix B rows.')
        self.result = zero(self.lenx, self.leny_)
        for i in range(self.lenx):
            for j in range(self.leny_):
                total = 0
                for z in range(self.lenx_):
                    total += self.x[i][z] * self.y[z][j]
                self.result[i][j] = total
        if len(self.result[0]) > 2:
            self.z = True
        return self.result

    # FUNCTION TWO ADD MATRICES
    def add(self, x=None, y=None):

        if x is not None:
            self.__init__(x, y)
        for i in range(self.lenx):
            for j in range(self.lenx_):
                self.result[i][j] = self.x[i][j] + self.y[i][j]
        return self.result

    # FUNCTION TWO SUBTRACT MATRICES
    def sub(self, x=None, y=None):

        if x is not None:
            self.__init__(x, y)
        for i in range(self.lenx):
            for j in range(self.lenx_):
                self.result[i][j] = self.x[i][j] - self.y[i][j]
        return self.result

    # GRAPH THE ADDITION, SUBTRACTION AND MULTIPLICATION OF VECTORS IN A MATRIX.
    def graph(self, operation):
        if operation == 'add':
            self.add()
        elif operation == 'sub':
            self.sub()
        elif operation == 'mult':
            self.mult()
        for i in self.x:
            if self.z is None:
                self.xpoints.append(i[0])
                self.ypoints.append(i[1])
            else:
                self.xpoints.append(i[0])
                self.ypoints.append(i[1])
                self.zpoints.append(i[2])
        for i in self.y:
            if self.z is None:
                self.xpoints.append(i[0])
                self.ypoints.append(i[1])
            else:
                self.xpoints.append(i[0])
                self.ypoints.append(i[1])
                self.zpoints.append(i[2])
        for i in self.result:
            if self.z is None:
                self.xpoints_result.append(i[0])
                self.ypoints_result.append(i[1])
            else:
                self.xpoints_result.append(i[0])
                self.ypoints_result.append(i[1])
                self.zpoints_result.append(i[2])

        if self.z is not None:
            fig = plt.figure()
            ax = plt.axes(projection="3d")
            ax.scatter3D(self.xpoints, self.ypoints, self.zpoints, s=35, color='blue')
            ax.scatter3D(self.xpoints_result, self.ypoints_result, self.zpoints_result, color='green', s=100,
                         marker="^")
            if operation == 'add':
                plt.title('Vector Addition of matrix')
            if operation == 'sub':
                plt.title('Vector Subtraction of matrix')
            if operation == 'mult':
                plt.title('Vector Multiplication of matrix')
            for i in range(len(self.zpoints_result)):
                ax.text(self.xpoints_result[i], 1.05 * self.ypoints_result[i], 1.05 * self.zpoints_result[i],
                        f'{(self.xpoints_result[i], self.ypoints_result[i], self.zpoints_result[i])}')
            for i in range(len(self.zpoints)):
                ax.text(self.xpoints[i], 1.05 * self.ypoints[i], 1.05 * self.zpoints[i],
                        f'{(self.xpoints[i], self.ypoints[i], self.zpoints[i])}', alpha=0.5)
            for i in range(len(self.xpoints) // 2):
                try:
                    plt.plot([self.xpoints[i], self.xpoints[i + 2]], [self.ypoints[i], self.ypoints[i + 2]],
                             [self.zpoints[i], self.zpoints[i + 2]], color='blue',
                             alpha=0.4, linestyle='--')
                except:
                    pass
            for i in range(len(self.xpoints) // 2):
                try:
                    print(self.xpoints[i], self.xpoints[i + 1], self.xpoints[i + 2])
                    plt.plot([self.xpoints[i], self.xpoints_result[i]], [self.ypoints[i], self.ypoints_result[i]],
                             [self.zpoints[i], self.zpoints_result[i]],
                             color='blue', alpha=0.4)
                    plt.plot([self.xpoints[i + 2], self.xpoints_result[i]],
                             [self.ypoints[i + 2], self.ypoints_result[i]],
                             [self.zpoints[i + 2], self.zpoints_result[i]],
                             color='blue', alpha=0.4)
                except:
                    print('err')
            plt.legend()
            plt.show()
        else:
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.grid(True, alpha=0.25)
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('center')
            if operation == 'sub':
                ax.set_xlim(-max(self.xpoints) * 1.25, max(self.xpoints) * 1.25)
                ax.set_ylim(-max(self.ypoints) * 1.25, max(self.ypoints) * 1.25)
            else:
                ax.set_xlim(-max(self.xpoints_result) * 1.25, max(self.xpoints_result) * 1.25)
                ax.set_ylim(-max(self.ypoints_result) * 1.25, max(self.ypoints_result) * 1.25)
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            yticks = ax.yaxis.get_major_ticks()
            yticks[len(yticks) // 2].label1.set_visible(False)
            xticks = ax.xaxis.get_major_ticks()
            xticks[len(xticks) // 2].label1.set_visible(False)
            ax.scatter(self.xpoints, self.ypoints, s=35, label='Before')
            ax.scatter(self.xpoints_result, self.ypoints_result, color='green', s=80, marker="^", label='After')
            if operation == 'add':
                plt.title('Vector Addition of a matrix')
            if operation == 'sub':
                plt.title('Vector Subtraction of a matrix')
            for i in range(len(self.xpoints_result)):
                ax.text(self.xpoints_result[i], 1.05 * self.ypoints_result[i],
                        f'{(self.xpoints_result[i], self.ypoints_result[i])}')
            for i in range(len(self.xpoints) // 2):
                try:
                    plt.plot([self.xpoints[i], self.xpoints[i + 2]], [self.ypoints[i], self.ypoints[i + 2]],
                             color='blue', alpha=0.4, linestyle='--')
                except:
                    pass
            for i in range(len(self.xpoints) // 2):
                try:
                    plt.plot([self.xpoints[i], self.xpoints_result[i]], [self.ypoints[i], self.ypoints_result[i]],
                             color='blue', alpha=0.4)
                    plt.plot([self.xpoints[i + 2], self.xpoints_result[i]],
                             [self.ypoints[i + 2], self.ypoints_result[i]],
                             color='blue', alpha=0.4)
                except:
                    pass
            plt.legend()
            plt.show()

    # CALCULATE DETERMINANT.
    '''TO DO: IMPLEMENT DETERMINANT FINDING ALGORITHM INSTEAD OF USING NUMPY'''
    def det(self, graph=None):
        value = np.linalg.det(self.x)
        if graph == 'True':
            self.result = self.mult(self.x, [[0], [1]])
            self.xpoints_result.append(self.result[0][0])
            self.ypoints_result.append(self.result[1][0])
            self.result = self.mult(self.x, [[1], [0]])
            self.xpoints_result.append(self.result[0][0])
            self.ypoints_result.append(self.result[1][0])
            self.result = self.mult(self.x, [[0], [0]])
            self.xpoints_result.append(self.result[0][0])
            self.ypoints_result.append(self.result[1][0])
            self.result = self.mult(self.x, [[1], [1]])
            self.xpoints_result.append(self.result[0][0])
            self.ypoints_result.append(self.result[1][0])
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.grid(True, alpha=0.25)
            ax.spines['left'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('center')
            ax.set_xlim(-2.5 * max(self.xpoints_result), 2.5 * max(self.xpoints_result))
            ax.set_ylim(-2.5 * max(self.ypoints_result), 2.5 * max(self.ypoints_result))
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            yticks = ax.yaxis.get_major_ticks()
            yticks[len(yticks) // 2].label1.set_visible(False)
            xticks = ax.xaxis.get_major_ticks()
            xticks[len(xticks) // 2].label1.set_visible(False)
            ax.scatter(self.xpoints_result, self.ypoints_result, color='blue', alpha=0.5, s=80, marker=".")
            verts = list(zip(self.xpoints_result, self.ypoints_result))
            verts.sort()
            verts[3], verts[2] = verts[2], verts[3]
            verts.insert(4, verts[0])
            for i in verts:
                print(i)
            codes = [
                Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO,
            ]
            path = Path(verts, codes)
            patch = patches.PathPatch(path, facecolor='orange', lw=2)
            ax.add_patch(patch)
            ax.text(1.30 * max(self.xpoints_result), 1.35 * max(self.ypoints_result), f'Determinant: {int(value)}',
                    size=15,
                    fontweight='light')
            plt.show()
        return value


a = Matrix([[2, 3, 1], [1, 2, 3]], [[1, 5, 6], [1, 0, 2]])
# print(a.det('True'))
# a.graph('sub')
# a.add()
# a.sub()
# a.mult()
