import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { CheckGridResponse, GetArg, SudokuGridRequest, SudokuGridResponse, SudokuList } from './types'

export const reducerPath = 'sudokus'

export const sudokusApi = createApi({
  reducerPath,
  baseQuery: fetchBaseQuery({ baseUrl: '/api/' }),
  tagTypes: ['Sudokus'],
  endpoints: (builder) => ({
    listSudokus: builder.query<SudokuList, void>({
      query: () => 'sudokus',
      providesTags: ['Sudokus']
    }),
    getSudoku: builder.query<SudokuGridResponse, GetArg>({
      query: ({ id }) => `sudoku?id=${id}`
    }),
    checkSolution: builder.mutation<CheckGridResponse, SudokuGridRequest>({
      query: ({ id, board }) => {
        return {
          url: `sudoku/check?id=${id}`,
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

export const { useListSudokusQuery, useGetSudokuQuery, useCheckSolutionMutation } = sudokusApi
