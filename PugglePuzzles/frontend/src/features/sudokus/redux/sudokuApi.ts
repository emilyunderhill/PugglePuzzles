import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { CheckGridRequest, CheckGridResponse, GetGridArg, GetListArg, SaveProgressRequest, SudokuGridResponse, SudokuList } from './types'

export const reducerPath = 'sudokus'

export const sudokusApi = createApi({
  reducerPath,
  baseQuery: fetchBaseQuery({ baseUrl: '/api/sudokus' }),
  tagTypes: ['Sudokus'],
  endpoints: (builder) => ({
    listSudokus: builder.query<SudokuList, GetListArg>({
      query: ({ date }) => date ? `/all?date=${date}` : '/all',
      providesTags: ['Sudokus']
    }),
    getSudoku: builder.query<SudokuGridResponse, GetGridArg>({
      query: ({ date }) => date ? `/get?date=${date}` : '/get'
    }),
    saveProgress: builder.mutation<void, SaveProgressRequest>({
      query: ({ id, board }) => {
        return {
          url: `/save`,
          method: 'POST',
          body: {
            id,
            board
          }
        }
      }
    }),
    checkSolution: builder.mutation<CheckGridResponse, CheckGridRequest>({
      query: ({ id, board }) => {
        return {
          url: `/check`,
          method: 'POST',
          body: {
            id,
            board
          }
        }
      },
      invalidatesTags: ['Sudokus']
    }),
  }),
})

export const { useListSudokusQuery, useGetSudokuQuery, useCheckSolutionMutation, useSaveProgressMutation } = sudokusApi
