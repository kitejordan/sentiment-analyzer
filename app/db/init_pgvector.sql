create extension if not exists vector;

create table if not exists documents (
  id bigserial primary key,
  text text not null,
  aspect_hint varchar(128),
  sentiment_label varchar(16),
  category varchar(64),
  flags jsonb,
  embedding vector(1536) not null
);

create table if not exists reviews (
  id bigserial primary key,
  text text not null,
  product_category varchar(64),
  rating int
);

create table if not exists aspects (
  id bigserial primary key,
  review_id bigint references reviews(id) on delete cascade,
  aspect_term varchar(128) not null,
  sentiment varchar(16) not null,
  confidence float,
  method varchar(16) not null
);

create table if not exists retrieved_evidence (
  id bigserial primary key,
  aspect_id bigint references aspects(id) on delete cascade,
  evidence_text text not null,
  similarity_score float not null,
  source_document_id bigint
);
