/**
 * Cirular Queue Library
 *
 * @note    The queue size can be defined ahead for strict memory control
 *          in embedded systems.
 *
 * @attention
 *          *****        DO NOT CHANGE THIS FILE           *****
 *          ***** Automatically Generated by IMU Assistant *****
 *
 *
 * @version V1.0     - Nov 10, 2014 - Creation
 *          V1.0 (R) - Jul 27, 2016 - Release Version.
 *
 * @section Example
 * @code
        #include "EasyLib/EasyQueue.h"

        int main()
        {
            EasyQueue<char> inQueue;
            inQueue.resize(256);
            inQueue.push( 123 );
            inQueue.push( 456 );
            while( ! inQueue.empty() ){
                char c = inQueue.front(); // Read first element of the queue
                inQueue.pop();            // Delete first element of the queue
            }
            return 0;
        }
 * @endcode
 *
 * @attention
 * <h2><center>&copy; COPYRIGHT(c) 2017 SYD Dynamics ApS</center></h2>
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *   1. Redistributions of source code must retain the above copyright notice,
 *      this list of conditions and the following disclaimer.
 *   2. Redistributions in binary form must reproduce the above copyright notice,
 *      this list of conditions and the following disclaimer in the documentation
 *      and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef EASYQUEUE_H
#define EASYQUEUE_H

//#define DEBUG_EASY_QUEUE_

#ifdef DEBUG_EASY_QUEUE_
#   include <stdio.h>
#endif

#include <stdlib.h> // for calloc(), free()


template<typename QueueDataType>
class EasyQueue
{
public:
    EasyQueue()
    {
        queueSize = 32+1;
        queueStart= 0;
        queueEnd  = 0;
        queueData = (QueueDataType*)calloc(queueSize, sizeof(QueueDataType) );
    }


    /**
      * Resize Queue
      * @return 1:Succ 0:fail
      */
    int resize(int bufSize)
    {
        queueSize = bufSize+1;
        queueStart= 0;
        queueEnd  = 0;
        queueData = (QueueDataType*)realloc(queueData, queueSize * sizeof(QueueDataType));
        if(queueData) return 1;
        else return 0;
    }


    ~EasyQueue(){
        free(queueData);
    }


    /**
     * Push data into Queue Tail.
     * @return  0  The queue is not full
     *          1  The queue is full. Queue Head maybe overwritten.
     */
    int push(QueueDataType data){
        int full = 0;

        queueData[queueEnd++] = data;

        if(queueEnd >= queueSize) queueEnd = 0;
        if(queueEnd == queueStart){
            full = 1;
            if((++queueStart) >= queueSize) queueStart = 0;
        }
        return full;
    }


    /**
     * Check if queue is empty or not
     * @return  1  Is empty
     *          0  Is not empty
     */
    int empty(void){
        if(queueEnd == queueStart) return 1;
        else return 0;
    }


    /**
     * Read Queue head (without deleting it)
     * @return  The queue head
     */
    QueueDataType front(void){
        return queueData[queueStart];
    }


    /**
     * Delete Queue head. (If queue is empty, nothing happens)
     */
    void pop(void){
        if(empty()) return;
        if((++queueStart) >= queueSize) queueStart = 0;
    }


    /**
     * Debug Print
     */
    void print(void){
    #   ifdef DEBUG_EASY_QUEUE_
        int i;
        printf("\nQueue: ");

        for(i=0; i<queueSize; i++){
            if(i==queueStart)
                printf(" [");
            printf(" %d ", (int)(queueData[i]));
            if(i==queueEnd)
                printf("] ");
        }

        if( Queue_Empty() ){
            printf(" Empty ");
        }
        printf("\n ");
    #   endif
    }


private:
    QueueDataType* queueData;
    int queueSize;
    int queueStart, queueEnd;
};

#endif // EASYQUEUE_H
