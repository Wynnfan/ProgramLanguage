#--coding:utf-8--
'''
������20��
��Ŀ��һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룻�����£�������
��������10�����ʱ�������������ף���10�η�����ߣ�
'''
Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2

print 'Total of road is %f' % Sn
print 'The tenth is %f meter' % Hn