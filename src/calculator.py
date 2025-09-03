import sys
import logging
logger = logging.getLogger(__name__)

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def test(self, pageNum):
        pageIdxInOrder = 0

        if (pageNum < 20):
            pageIdxInOrder = pageNum & 0x3
            pStartPageOfOrder = pageNum - pageIdxInOrder
            pPageCntOfCurOrder = 4
        elif (pageNum < 4336):
            curOrder = ((pageNum - 20) >> 2) + 5

            if (curOrder & 0x1):
                pStartPageOfOrder = 0 + (((curOrder - 5) >> 1) << 2)
            else:
                pStartPageOfOrder = 20 + (((curOrder - 6) >> 1) << 2)

            pageIdxInOrder = pageNum & 0x3
            pPageCntOfCurOrder = 4
        elif (pageNum < 4360):
            ofs = (pageNum - 4336) % 0x6
            if (ofs < 2):
                pageIdxInOrder = ofs
                pStartPageOfOrder = 2176 + (int(((pageNum) - 4336) / 0x6) << 1)
                pPageCntOfCurOrder = 2
            else:
                pageIdxInOrder = ofs - 2
                pStartPageOfOrder = 2160 + (int((pageNum - 4336) / 0x6) << 2)
                pPageCntOfCurOrder = 4
        elif (pageNum < 4376):
            pageIdxInOrder = (pageNum - 4360) & 0x1
            pStartPageOfOrder = 2184 + (((pageNum - 4360) >> 1) << 1)
            pPageCntOfCurOrder = 2
        elif (pageNum < 4396):
            pageIdxInOrder = (pageNum - 4376) & 0x3
            pStartPageOfOrder = 2200 + (((pageNum - 4376) >> 2) << 2)
            pPageCntOfCurOrder = 4
        elif (pageNum < 8776):
            curOrder = ((pageNum - 4396) >> 2) + 1105

            if (curOrder & 0x1):
                pStartPageOfOrder = 2200 + (((curOrder - 1105) >> 1) << 2)
            else:
                pStartPageOfOrder = 2220 + (((curOrder - 1106) >> 1) << 2)

            pageIdxInOrder = pageNum & 0x3
            pPageCntOfCurOrder = 4
        elif (pageNum < 8800):
            ofs = (pageNum - 8776) % 0x6
            if (ofs < 2):
                pageIdxInOrder = ofs
                pStartPageOfOrder = 4408 + (int((pageNum - 8776) / 0x6) << 1)
                pPageCntOfCurOrder = 2
            else:
                pageIdxInOrder = ofs - 2
                pStartPageOfOrder = 4392 + (int((pageNum - 8776) / 0x6) << 2)
                pPageCntOfCurOrder = 4
        else:
            assert(0)

        logger.info("pageNum:%d pageIdxInOrder:%d pStartPageOfOrder:%d pPageCntOfCurOrder:%d", pageNum, pageIdxInOrder, pStartPageOfOrder, pPageCntOfCurOrder)
        

    def N69R_ProgramOrd_2_PhyPage(self, progOrd):
        if (progOrd < 5):
            pageAdr = (progOrd << 2)
        elif (progOrd < 1084):
            if (progOrd & 0x01):
                pageAdr = 0 + (((progOrd - 5) >> 1) << 2)
            else:
                pageAdr = 20 + (((progOrd - 6) >> 1) << 2)
        elif (progOrd < 1092):
            if (progOrd & 0x01):
                pageAdr = 0 + (((progOrd - 5) >> 1) << 2)
            else:
                pageAdr = 2176 + (((progOrd - 1084) >> 1) << 1)
        elif(progOrd < 1100):
            pageAdr =  2184 + ((progOrd - 1092) << 1)
        elif (progOrd < 1105):
            pageAdr = 2200 + ((progOrd - 1100) << 2)
        elif (progOrd < 2200):
            if (progOrd & 0x01):
                pageAdr = 2200 + (((progOrd - 1105) >> 1) << 2)
            else:
                pageAdr = 2220 + (((progOrd - 1106) >> 1) << 2)
        elif (progOrd < 2208):
            if (progOrd & 0x01):
                pageAdr = 2200 + (((progOrd - 1105) >> 1) << 2)
            else:
                pageAdr = 4408 + (((progOrd - 2200) >> 1) << 1)
        else:
            assert(0)
        logger.info("progOrd:%d pageAdr:%d", progOrd, pageAdr)

    def N69R_RealPage2OrderPage(self, RealPageNum):
        if (RealPageNum < 2160):
            orderIdx = (RealPageNum >> 2)
            pageIdxInOrder = RealPageNum & 0x3
            OrderPageNum = 20 + (orderIdx << 3) + pageIdxInOrder
        elif (RealPageNum < 2176):
            orderIdx = (RealPageNum - 2160) >> 2
            pageIdxInOrder = ((RealPageNum - 2160) & 0x3) + 2
            OrderPageNum = 4340 + (orderIdx * 6) + pageIdxInOrder
        else:
            assert(0)
        logger.info("RealPageNum:%d orderIdx:%d OrderPageNum:%d", RealPageNum, orderIdx, OrderPageNum)

    def N69R_WordLineNum_2_PageNum(self, WordLineNum, CellType):
        if (WordLineNum < 544):
            PageNum = WordLineNum * 4 + (CellType - 1)
        elif (WordLineNum < 556):
            PageNum = 2176 + (WordLineNum - 544) * 2 + (CellType - 1)
        elif (WordLineNum < 1108):
            PageNum = 2200 + (WordLineNum - 556) * 4 + (CellType - 1)
        elif(WordLineNum < 1112):
            PageNum = 4408 + (WordLineNum - 1108) * 2 + (CellType - 1)
        else:
            assert(0)
        logger.info("WL:%d CT:%d PageNum:%d", WordLineNum, CellType, PageNum)


    def PAA_2_FAA(self, BS, AU, is6PAs4P = 0):
        if is6PAs4P == 0:
            BS = 1
        else:
            blk = int(BS * 4 / 6) * 8 + BS * 4 % 6
        logger.info("BS:0x%x -> Blk:0x%x Plane:0x%x", BS, blk, BS * 4 % 6)     

    def BS_2_Blk(self, BS, PlaneNum, is6PAs4P = 0):
        if is6PAs4P != 0:
            assert(PlaneNum == 6)
            BlkNumInAllPlane = BS * 4
            PlaneNumInBS = 4
        else:
            BlkNumInAllPlane = BS * PlaneNum
            PlaneNumInBS = PlaneNum

        
        for idx in range(0, PlaneNumInBS):
            blk = int(BlkNumInAllPlane / PlaneNum) * PlaneNum + (BlkNumInAllPlane % PlaneNum)           # 逻辑Blk，没有计算中间的空缺
            blkAtRow = int(BlkNumInAllPlane / PlaneNum) * 8 + (BlkNumInAllPlane % PlaneNum)             # 仅适用于6Plane颗粒
            logger.info("[%d]Blk:0x%x(%d) Plane:0x%x . If 6Plane:BlkAtRow:0x%x[%d]", idx, blk, blk, (BlkNumInAllPlane % PlaneNum),blkAtRow,blkAtRow)
            BlkNumInAllPlane = BlkNumInAllPlane + 1
        
    def Blk_2_BS(self, Blk, PlaneNum, is6PAs4P = 0, isBlkAtRow = 0):
        if is6PAs4P != 0:
            assert(PlaneNum == 6)
            if isBlkAtRow != 0:
                BlkNumInAllPlane = int(Blk / 8) * 6 + (Blk % 8)     # 先转化一下，按照紧密排列的情况下，所有Plane的排序
                Blk = BlkNumInAllPlane
            BS = int(Blk / 4)
        else:
            BS = int(Blk / PlaneNum)
        logger.info("BS:0x%x(%d)", BS, BS)
        self.BS_2_Blk(BS, PlaneNum, is6PAs4P)

    '''
    统计两个文件中bit位存在差异的数量,unit:bit
    file1、file2:两个文件的路径
    '''
    def count_different_bits(self, file1, file2):
        # 读取两个文件
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            data1 = f1.read()
            data2 = f2.read()
        
        # 确定最小长度
        min_len = min(len(data1), len(data2))
        total_bits = min_len * 8
        
        # 统计不同比特数
        different_bits = 0
        
        # 比较相同长度部分
        for i in range(min_len):
            byte1 = data1[i]
            byte2 = data2[i]
            
            # 比较每个比特，异或取出bit不一样的位置
            xor_result = byte1 ^ byte2
            # 计算不同比特数
            different_bits += bin(xor_result).count('1')
        
        # 处理长度不同的情况
        if len(data1) != len(data2):
            # longer_data = data1 if len(data1) > len(data2) else data2
            extra_bytes = abs(len(data1) - len(data2))
            
            # 多出的部分每个字节的所有比特都视为不同
            different_bits += extra_bytes * 8
            total_bits += extra_bytes * 8
            logger.info("lenth diff %d byte %d bit.file1:%d file2::%d", extra_bytes, different_bits, len(data1), len(data2))
        
        return different_bits, total_bits

        
        

            