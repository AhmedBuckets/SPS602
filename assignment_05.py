import numpy as np, pandas as pd, matplotlib.pyplot as plt
import unittest
import requests
import json


def exercise01():
    df = pd.DataFrame(np.random.randint(0,100,size=(3, 4)))
    return df

def exercise02(a):
    array = np.array(a)
    return array

def exercise03(a):
    sum = np.sum(a)
    return sum

def exercise04(a):
    sum = np.sum(a[:,1])
    return sum

def exercise05(n):
    zeros = np.zeros((n,n))
    return zeros

def exercise06(n):
    ones = np.ones((n,n))
    return ones

def exercise07(sd,m,s):
    random_numbers = np.random.normal(m, sd, s)
    return random_numbers

def exercise08():
    url = "https://tinyurl.com/y63q7okz"
    df = pd.read_csv(url)
    row_count = df.shape[0]
    avg_sq_ft = df['sq__ft'].mean()
    df_zip_95670 = df[df['zip'] == 95670]
    df_zip_not_95610 = df[df['zip'] != 95610]
    return df, row_count, avg_sq_ft, df_zip_95670, df_zip_not_95610

def exercise10(n):
    identity_matrix = np.eye(n)
    return identity_matrix

def exercise11(n):
    array_1d = np.arange(n)
    array_reshaped = array_1d.reshape(3, -1)
    return array_1d, array_reshaped

def exercise12(n):
    checkerboard_matrix = np.tile(np.array([[1,0],[0,1]]), (n,n))
    return checkerboard_matrix

def exercise13(n):
    s = pd.Series(np.random.randint(0, n, n), index=pd.date_range('2010-01-01', periods=n))
    s.cumsum().plot()
    plt.show()
    return s

def exercise14(words):
    df = pd.Series(words).map(lambda x: len(x))
    return df

def exercise15():
    url = "https://tinyurl.com/y63q7okz"
    df = pd.read_csv(url)
    df = df.iloc[::5, :][['street', 'zip']]
    return df

class TestAssignment5(unittest.TestCase):
    def test_exercise15(self):
        print('Skipping exercise 15')
        df = exercise15()
        print(df)
    
    def test_exercise14(self):
        print('Skipping exercise 14')
        df = exercise14(['cat','frog','walrus','antelope'])
        print(df)

    def test_exercise13(self):
        print('Testing exercise 13')
        s= exercise13(1000)
        self.assertEqual(s.index[0],pd.Timestamp('2010-01-01 00:00:00'))
        self.assertEqual(len(s.index),1000)

    def test_exercise12(self):
        print('Testing exercise 12')
        cm = exercise12(10)
        self.assertEqual(cm.shape[0],20)
        self.assertEqual(cm[0,0],1)
        self.assertEqual(cm[0,1],0)
        cm = exercise12(5)
        self.assertEqual(cm.shape[0],10)
        self.assertEqual(cm[0,0],1)
        self.assertEqual(cm[0,1],0)        


    def test_exercise11(self):
        print('Testing exercise 11')
        a1d, ar = exercise11(15)
        self.assertEqual(a1d.shape[0],15)
        self.assertEqual(ar.shape[0],3)
        self.assertEqual(ar.shape[1],5)

    def test_exercise10(self):
        print('Testing exercise 10')
        im = exercise10(10)
        self.assertEqual(im.shape[0],10)
        self.assertEqual(im.shape[1],10)


        

    def test_exercise08(self):
        print('Testing exercise 8')
        df, row_count, avg_sq_ft, df_zip_95670, df_zip_not_95610 = exercise08()
        self.assertEqual(df.shape[0],985)
        self.assertEqual(df.shape[1],12)
        self.assertEqual(row_count,985)
        self.assertAlmostEqual(avg_sq_ft,1314.91675127,2)
        self.assertEqual(df_zip_95670.shape[0],21)
        self.assertEqual(df_zip_not_95610.shape[0],978)
 
    
    def test_exercise07(self):
        print('Testing exercise 7')
        z = exercise07(10,5,100000)
        self.assertEqual(z.shape[0], 100000)
        self.assertLessEqual(np.average(z), 5.2)
        self.assertGreaterEqual(np.average(z), 4.7)
        z = exercise07(5,10,100000)
        self.assertEqual(z.shape[0], 100000)
        self.assertLessEqual(np.average(z), 10.2)
        self.assertGreaterEqual(np.average(z), 9.7)


    def test_exercise06(self):
        print('Testing exercise 6')
        z = exercise06(7).shape
        self.assertEqual(z[0], 7)
        self.assertEqual(z[1], 7)
        z = exercise05(70).shape
        self.assertEqual(z[0], 70)
        self.assertEqual(z[1], 70)
        

    def test_exercise05(self):
        print('Testing exercise 5')
        z = exercise05(7).shape
        self.assertEqual(z[0], 7)
        self.assertEqual(z[1], 7)
        z = exercise05(70).shape
        self.assertEqual(z[0], 70)
        self.assertEqual(z[1], 70)

    def test_exercise04(self):
        print('Testing exercise 4')
        array = np.array([[1,1,1,1,1],[0,2,0,0,1]])
        sum = exercise04(array)
        self.assertEqual(sum, 3)
        array = np.array([[1,6,1,1,1],[0,2,0,0,1]])
        sum = exercise04(array)
        self.assertEqual(sum, 8)

    def test_exercise03(self):
        print('Testing exercise 3')
        array = np.array([1,1,1,1,1])
        sum = exercise03(array)
        self.assertEqual(sum, 5)
        array = np.array([2,4])
        sum = exercise03(array)
        self.assertEqual(sum, 6)

    def test_exercise01(self):
        print('Testing exercise 1')
        m = exercise01().shape
        self.assertEqual(m[0], 3)
        self.assertEqual(m[1], 4)

    def test_exercise02(self):
        print('Testing exercise 2')
        m = exercise02([1,2,3,4,5,6])
        self.assertTrue(type(m) is np.ndarray)
        self.assertEqual(m.shape[0], 6)

if __name__ == '__main__':
    unittest.main()