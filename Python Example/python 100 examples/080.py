# -*- coding: UTF-8 -*-
'''
������80��
��Ŀ����̲����һ�����ӣ���ֻ�������֡���һֻ���Ӱ��������ƾ�ݷ�Ϊ��ݣ�����һ������ֻ
���������ӰѶ��һ�����뺣�У�������һ�ݡ��ڶ�ֻ���Ӱ�ʣ�µ�������ƽ���ֳ���ݣ��ֶ���
������һ������ͬ���Ѷ��һ�����뺣�У�������һ�ݣ����������ġ�����ֻ���Ӷ����������ģ�
�������ʺ�̲��ԭ�������ж��ٸ����ӣ�
1.���������
2.����Դ���룺
'''
if __name__ == '__main__':
    for i in range(4,10000,4):
        count = 0
        m = i
        for k in range(5):
            j = i / 4 * 5 + 1
            i = j
            if j % 4 == 0:
                count += 1
            else:
                break
        i = m
        if count == 4:
            print count
            break
        